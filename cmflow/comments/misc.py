import os
import re
from typing import List

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


def check_file(file_path: str) -> bool:
    if not file_path.endswith(".txt"):
        return False

    file_size = os.path.getsize(file_path)
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


def scale_image(image_path: str, max_width: int, max_height: int) -> None:
    with Image.open(image_path) as img:
        ratio = min(max_width / img.width, max_height / img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))

        img = img.resize(new_size, Image.ANTIALIAS)
        img.save("scaled_" + image_path)
