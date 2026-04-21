from django.urls import path, include
from django.test import override_settings


def crash_view(request):
    raise Exception("Erreur volontaire pour le test")


urlpatterns = [
    path("", include('oc_lettings_site.urls')),
    path("test-500/", crash_view),
]


def test_unknown_url_returns_404(client):
    response = client.get('/elt-does-not-exist/')
    assert response.status_code == 404
    assert b"404" in response.content
    assert b"Page not found" in response.content


@override_settings(ROOT_URLCONF=__name__, DEBUG=False)
def test_crash_view_returns_500(client):
    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert response.status_code == 500
    assert b"500" in response.content
    assert b"Server error" in response.content
