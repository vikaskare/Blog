from django.urls import path
from .views import all_post, get_post, create_post, update_post, delete_post

urlpatterns = [
    path("", view=all_post, name="all_post"),
    path("create/", view=create_post, name="create_post"),
    path("<int:pk>/", view=get_post, name="get_post"),
    path("<int:pk>/update", view=update_post, name="update_post"),
    path("<int:pk>/delete", view=delete_post, name="delete_post"),
]
