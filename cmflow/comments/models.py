from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    home_page_url = models.URLField(blank=True, null=True)


class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(
        Comment, related_name="attachments", on_delete=models.CASCADE
    )
    file_path = models.FileField(upload_to="attachments/")
    file_type = models.CharField(max_length=50)


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
