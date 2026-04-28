"""
Integration tests for the views of the profiles application.
This module validates the HTTP Responses and rendered content for
the index and detail views.
"""

import pytest
import logging
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse
from django.http import Http404
from django.test import RequestFactory


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


def test_profiles_index_logs_info_message(client, caplog):
    """
    Verify that the profiles index view writes an info log.

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    create_profile(username="johnny", favorite_city="Firenze")
    with caplog.at_level(logging.INFO):
        response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assert "Profiles index page requested" in caplog.text


def test_profile_detail_logs_warning_for_unknown_username(client, caplog):
    """
    Verify that an unknown username writes a warning log.

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    with caplog.at_level(logging.WARNING):
        response = client.get(reverse("profiles:profile_detail", args=["bob"]))
    assert response.status_code == 404
    assert "Profile not found" in caplog.text


def test_profile_detail_logs_warning_for_invalid_username(caplog):
    """
    Verify that an invalid username writes a warning log.

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    request = RequestFactory().get("/profiles/%20/")
    with caplog.at_level(logging.WARNING):
        with pytest.raises(Http404):
            from profiles.views import profile_detail
            profile_detail(request, " ")
    assert "Invalid username received: " in caplog.text
