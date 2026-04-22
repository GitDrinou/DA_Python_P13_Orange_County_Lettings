"""
Integration tests for the views of the main application.
This module validates the HTTP Responses and rendered content for
the index view.
"""

import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_home_page_returns_200(client):
    """
    Verify that the home page returns 200.
    This test ensures that the index view of the main application
    respond with a status code = 200 (Success).

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    response = client.get(reverse("index"))
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
    response = client.get(reverse("profiles:profile", args=["bob"]))
    assert response.status_code == 404
