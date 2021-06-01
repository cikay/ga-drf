
from django.conf.urls import url
from .views import AuthorView


urlpatterns = [
    url(r"^create/$", AuthorView.as_view())
]