from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def all_post(request, *args, **kwargs):
    posts = Post.objects.all().order_by("-updated_at")
    return render(request, template_name="post/all.html", context={"posts": posts})


def get_post(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    return render(request, template_name="post/view.html", context={"post": post})


def create_post(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_post")
        else:
            return render(
                request=request,
                template_name="post/create.html",
                context={"form": form},
            )
    else:
        form = PostForm()
        return render(
            request=request, template_name="post/create.html", context={"form": form}
        )


def update_post(request, pk, *args, **kwargs):
    obj = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("post", pk)
    return render(
        request=request,
        template_name="post/update.html",
        context={"form": form, "id": pk},
    )


def delete_post(request, pk, *args, **kwargs):
    obj = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("all_post")
    return render(request=request, template_name="post/delete.html", context={"id": pk})
