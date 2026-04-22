"""
Unit tests for the URL configuration of the profiles application.
this module verifies that the named routes generate the expected paths and
the correct view functions.
"""

from django.urls import resolve, reverse
from profiles.views import index, profile_detail


def test_profiles_index_url_resolve():
    """
    Verify that the profiles index URL resolves correctly.
    This test ensures that the 'profiles:index' named route generates the
    expected path and view function.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: It the generated URL or view is incorrect.
    """
    url = reverse("profiles:index")
    assert url == "/profiles/"
    assert resolve(url).func == index


def test_profiles_detail_url_resolve():
    """
    Verify that the profiles detail URL resolves correctly.
    This test ensures that the 'profiles:profile' named route generates the
    expected path and view function.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: It the generated URL or view is incorrect.
    """
    url = reverse("profiles:profile", args=["Bob"])
    assert url == "/profiles/Bob/"
    assert resolve(url).func == profile_detail
