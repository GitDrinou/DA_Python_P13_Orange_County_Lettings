"""
Integration tests for the views of the profiles application.
This module validates the HTTP Responses and rendered content for
the index and detail views.
"""

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


pytestmark = pytest.mark.django_db


def create_profile(
        username="johnny",
        favorite_city="Firenze"
):
    """
    Create and return a profile object for testing.
    This helper method creates a profile object with the provided values.

    Parameters:
         username (str): The username of the Django user
         favorite_city (str): The favorite city of the user
    Returns:
        Profile: the created profile object
    Raises:
        ValidationError: If one of the provided values is invalid when saved.
    """
    user = User.objects.create_user(username=username, password="TestPass123!")
    return Profile.objects.create(user=user, favorite_city=favorite_city)


def test_profiles_index_returns_200(client):
    """
    Verify that the profiles index page returns 200.
    This test ensures that the index view of the profiles application
    respond with a status code = 200 (Success).

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    create_profile(username="johnny", favorite_city="Firenze")
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200


def test_profiles_detail_returns_200(client):
    """
    Verify that the profiles detail page returns 200 for a valid identifier.
    This test ensures that the detail view of the profiles application
    respond with a status code = 200 (Success).

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    create_profile(username="johnny", favorite_city="Firenze")
    response = client.get(reverse("profiles:profile_detail",
                                  args=["johnny"]))
    assert response.status_code == 200


def test_profile_detail_returns_404_for_unknown_id(client):
    """
    Verify that the profile detail page returns 404 for unknown identifier.
    This test ensures that the non-existent profile respond with a status
    code = 404 (Not Found)

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 404.
    """
    response = client.get(reverse("profiles:profile_detail", args=["bob"]))
    assert response.status_code == 404
