from django.urls import path, include
from django.test import override_settings


def crash_view(request):
    """
    Raise an exception to simulate an internal server error.
    This test-only view is used to verify that the application correctly
    handles HTTP 500 errors and renders the custom error page.

    Parameters:
        request (HttpRequest): the incoming HTTP request
    """
    raise Exception("Erreur volontaire pour le test")


urlpatterns = [
    path("", include('oc_lettings_site.urls')),
    path("test-500/", crash_view),
]


def test_unknown_url_returns_404(client):
    """
    Verify that an unknown URL returns a 404 status code.
    This test ensures that the application returns the custom 404 error page
    when user tries to access a non-existent route.

    Parameters:
         client (Client): Django's test client

    Returns:
        None
    """
    response = client.get('/elt-does-not-exist/')
    assert response.status_code == 404
    assert b"404" in response.content
    assert b"Page not found" in response.content


@override_settings(ROOT_URLCONF=__name__, DEBUG=False)
def test_crash_view_returns_500(client):
    """
    Verify that an internal server error returns a 500 status code.
    This test ensures that the application returns the custom 500 error page
    when an unhandled exception occurs during request processing.

    Parameters:
        client (Client): Django's test client

    Returns:
         None
    """
    client.raise_request_exception = False
    response = client.get("/test-500/")
    assert response.status_code == 500
    assert b"500" in response.content
    assert b"Server error" in response.content
