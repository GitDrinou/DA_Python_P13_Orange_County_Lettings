"""
Integration tests for the views of the lettings application.
This module validates the HTTP Responses and rendered content for
the index and detail views.
"""

import pytest
from lettings.models import Address, Letting
from django.urls import reverse


pytestmark = pytest.mark.django_db


def create_letting(
        title="Cosy Apartment",
        number=10,
        street="Downtown Street",
        city="London",
        state="UK",
        zip_code=12345,
        country_iso_code="GB",
):
    """
    Create and return a letting object for testing.
    This helper method creates a letting object with the provided values.

    Parameters:
         title (str): the title of the letting
         number (int): the street number of the associated address
         street (str): the street name of the associated address
         city (str): the city of the associated address
         state (str): the state of the associated address
         zip_code (int): the zip code of the associated address
         country_iso_code (str): the country of the associated address
    Returns:
        Letting: the created letting object
    Raises:
        ValidationError: If one of the provided values is invalid when saved.
    """
    address = Address.objects.create(
        number=number,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,
        country_iso_code=country_iso_code,
    )
    return Letting.objects.create(
        title=title,
        address=address,
    )


def test_lettings_index_returns_200(client):
    """
    Verify that the lettings index page returns 200.
    This test ensures that the index view of the lettings application
    respond with a status code = 200 (Success).

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    create_letting(title="Charming living space")
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200


def test_lettings_detail_returns_200(client):
    """
    Verify that the lettings detail page returns 200 for a valid identifier.
    This test ensures that the detail view of the lettings application
    respond with a status code = 200 (Success).

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    letting = create_letting(title="Charming living space", number=10,
                             street="Downtown Street")
    response = client.get(reverse("lettings:letting",
                                  args=[letting.id]))
    assert response.status_code == 200


def test_letting_detail_returns_404_for_unknown_id(client):
    """
    Verify that the letting detail page returns 404 for unknown identifier.
    This test ensures that the non-existent letting respond with a status
    code = 404 (Not Found)

    Parameter:
        client (django.test.Client): Django test client uses for HTTP Request.
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 404.
    """
    response = client.get(reverse("lettings:letting", args=[999]))
    assert response.status_code == 404
