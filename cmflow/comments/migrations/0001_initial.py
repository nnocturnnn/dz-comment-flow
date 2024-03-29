# Generated by Django 5.0.1 on 2024-01-08 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "comment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),  # noqa: E501
                ("user_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("text", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("home_page_url", models.URLField(blank=True, null=True)),
                (
                    "parent_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="comments.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "attachment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),  # noqa: E501
                ("file_path", models.FileField(upload_to="attachments/")),
                ("file_type", models.CharField(max_length=50)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="comments.comment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "like_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),  # noqa: E501
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="comments.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
