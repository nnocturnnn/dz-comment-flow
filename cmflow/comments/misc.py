import os
import re
from io import BytesIO
from typing import List

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from google.cloud import storage
from lxml import html
from PIL import Image


def validate_html(content: str) -> bool:
    allowed_tags = ["a", "code", "i", "strong"]

    content = re.sub(
        r"<a([^>]*)>",
        lambda m: "<a"
        + re.sub(r' (?!href=|title=)[a-zA-Z\-]+="[^"]*"', "", m.group(1))
        + ">",
        content,
    )

    for tag in allowed_tags:
        if tag != "a":
            content = re.sub(rf"<{tag}[^>]*>", f"<{tag}>", content)
            content = re.sub(rf"</{tag}[^>]*>", f"</{tag}>", content)

    try:
        parsed = html.fromstring(content)
        html.tostring(parsed, method="xml")
        return True
    except Exception:
        return False


def check_file(file_obj) -> bool:
    if not file_obj.name.endswith(".txt"):
        return False

    file_size = file_obj.size
    if file_size > 100 * 1024:
        return False

    return True


def check_image_size(
    image_path: str, required_width: int, required_height: int
) -> bool:
    with Image.open(image_path) as img:
        if img.size == (required_width, required_height):
            return True
        else:
            return False


def check_image_format(image_path: str, allowed_formats: List[str]) -> bool:
    try:
        with Image.open(image_path) as img:
            if img.format in allowed_formats:
                return True
            else:
                return False
    except IOError:
        return False


def scale_image(
    image_file, max_width: int, max_height: int
) -> InMemoryUploadedFile:  # noqa: E501
    with Image.open(image_file) as img:
        ratio = min(max_width / img.width, max_height / img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

        image_io = BytesIO()
        img_format = (
            img.format if img.format else "PNG"
        )  # Default to PNG if format is unknown
        img.save(image_io, format=img_format)
        image_io.seek(0)

        # Create a new InMemoryUploadedFile
        new_image_file = InMemoryUploadedFile(
            file=image_io,
            field_name=image_file.field_name,
            name=image_file.name,
            content_type=f"image/{img_format.lower()}",
            size=image_io.getbuffer().nbytes,
            charset=None,
        )
        return new_image_file


def upload_to_bucket(blob_name, file_obj, content_type):
    """Upload file to Google Cloud Storage bucket."""
    storage_client = storage.Client.from_service_account_json(
        os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    )
    bucket = storage_client.bucket(settings.GS_BUCKET_NAME)
    blob = bucket.blob(blob_name)

    blob.upload_from_file(file_obj, content_type=content_type)
    blob.make_public()

    return blob.public_url
