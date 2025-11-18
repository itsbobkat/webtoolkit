from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "url-shortener/",
        views.URLShortenerView.as_view(),
        name="url_shortener",
    ),
    path(
        "file-hosting/",
        views.FileHostingView.as_view(),
        name="file_hosting",
    ),
    path(
        f"s/<slug:alias>",
        views.url_shortener_redirect,
        name="url_shortener_redirect",
    ),
    path(
        f"f/<str:alias_filename>",
        views.file_redirect,
        name="file_redirect",
    ),
    path(
        f"register/",
        views.RegisterView.as_view(),
        name="register",
    ),
]
