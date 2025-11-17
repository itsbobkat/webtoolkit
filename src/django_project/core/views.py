from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from . import models


# Create your views here.
def home(request):
    return render(request, "core/home.html")


class URLShortenerView(View):
    def get(self, request: HttpRequest):
        return render(request, "core/url_shortener.html")

    def post(self, request: HttpRequest):
        url = request.POST.get("url")
        created = models.ShortenedURL.create(url)
        shortened_url = request.build_absolute_uri(
            reverse(
                "core:url_shortener_redirect",
                kwargs={
                    "alias": created.alias,
                },
            )
        )

        return render(
            request, "core/url_shortener.html", {"shortened_url": shortened_url}
        )


def url_shortener_redirect(request, alias):
    if (request.method or "").lower() != "get":
        return HttpResponseNotFound()
    obj = get_object_or_404(
        models.ShortenedURL,
        alias=alias,
    )
    return redirect(obj.url)
