"""
Unit tests for the URL configuration of the lettings application.
this module verifies that the named routes generate the expected paths and
the correct view functions.
"""

from django.urls import resolve, reverse
from lettings.views import index, letting_detail


def test_lettings_index_url_resolve():
    """
    verify that the lettings index URL resolves correctly.
    This test ensures that the 'lettings:index' named route generates the
    expected path and view function.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: It the generated URL or view is incorrect.
    """
    url = reverse("lettings:index")
    assert url == "/lettings/"
    assert resolve(url).func == index


def test_lettings_detail_url_resolve():
    """
    verify that the lettings detail URL resolves correctly.
    This test ensures that the 'lettings:letting_detail' named route
    generates the
    expected path and view function.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: It the generated URL or view is incorrect.
    """
    url = reverse("lettings:letting_detail", args=["1"])
    assert url == "/lettings/1/"
    assert resolve(url).func == letting_detail
