"""
Unit test for the models of the profiles application.
This module validates the Profile model, including its string
representations and Django metadata.
"""
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


pytestmark = pytest.mark.django_db


def test_profile_str_returns_username():
    """
    Verify that the string representation of a profile is readable.
    This test ensure that the Profile model return the expected string with
    the username.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: If the string representation does not match the
        expected username.
    """
    user = User.objects.create_user(
        username="johnny",
        password="TestPass123!"
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city="Firenze",
    )
    assert str(profile) == "johnny"


def test_profile_verbose_name():
    """
    Verify the verbose names defined for the Profile model.
    This test ensure that the singular and plural verbose names are correct.

    Parameters:
        None
    Returns:
         None
    Raises:
        AssertionError: If the verbose names ar not correctly defined.
    """
    assert Profile._meta.verbose_name == "Profile"
    assert Profile._meta.verbose_name_plural == "Profiles"
