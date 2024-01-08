from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Attachment, Comment, Like  # noqa: F401


def base_view(request):
    comments_list = Comment.objects.all().order_by("-date_added")
    paginator = Paginator(comments_list, 25)

    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    for comment in comments:
        comment.like_count = Like.objects.filter(comment=comment).count()

    context = {
        "comments": comments,
    }
    return render(request, "test.html", context)


@require_http_methods(["POST"])
def comment_add(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def like_add(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def like_remove(request):
    return render(request, "index.html")
