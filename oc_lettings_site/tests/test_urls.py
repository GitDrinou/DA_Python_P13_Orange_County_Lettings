"""
Unit tests for the URL configuration of the main application.
this module verifies that the named routes generate the expected paths and
the correct view functions.
"""

from django.urls import resolve, reverse
from oc_lettings_site.views import index


def test_oc_index_url_resolve():
    """
    Verify that the index URL resolves correctly.
    This test ensures that the 'index' named route generates the
    expected path and view function.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: It the generated URL or view is incorrect.
    """
    url = reverse("index")
    assert url == "/"
    assert resolve(url).func == index
