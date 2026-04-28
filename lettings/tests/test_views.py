"""
Integration tests for the views of the lettings application.
This module validates the HTTP Responses and rendered content for
the index and detail views.
"""

import pytest
import logging
from lettings.models import Address, Letting
from django.urls import reverse
from django.http import Http404
from django.test import RequestFactory


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
    response = client.get(reverse("lettings:letting_detail",
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
    response = client.get(reverse("lettings:letting_detail", args=[999]))
    assert response.status_code == 404


def test_lettings_index_logs_info_message(client, caplog):
    """
    Verify that lettings index view writes an info log message.

    Parameter;
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200.
    """
    create_letting(title="Charming living space", number=10,
                   street="Downtown Street")
    with caplog.at_level(logging.INFO):
        response = client.get(reverse("lettings:index"))

    assert response.status_code == 200
    assert "Lettings index page requested" in caplog.text


def test_letting_detail_logs_warning_for_unknown_id(client, caplog):
    """
    Verify that an unknown letting identifier writes a warning log.

    Parameter;
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200
    """
    with caplog.at_level(logging.WARNING):
        response = client.get(reverse("lettings:letting_detail", args=[999]))
    assert response.status_code == 404
    assert "Letting not found" in caplog.text


def test_letting_detail_logs_warning_for_invalid_id(caplog):
    """
    Verify that an invalid letting identifier writes a warning log.

    Parameter;
        client (django.test.Client): Django test client uses for HTTP Request.
        caplog (django.test.utils.log.LogCaptured): LogCaptured object for
        capturing
    Returns:
        None
    Raises:
        AssertionError: If the response status code is not 200
    """
    request = RequestFactory().get("/lettings/0/")
    with caplog.at_level(logging.WARNING):
        with pytest.raises(Http404):
            from lettings.views import letting_detail
            letting_detail(request, 0)
    assert "Invalid letting id received: 0" in caplog.text
