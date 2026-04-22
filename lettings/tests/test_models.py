"""
Unit test for the models of the lettings application.
This module validates the Address and Letting models, including their
string representations and Django metadata.
"""
import pytest
from lettings.models import Address, Letting


pytestmark = pytest.mark.django_db


def test_address_str_returns_number_and_street():
    """
    Verify that the string representation of an address is readable.
    This test ensure that the Address model return the expected string with
    street number and street name.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: If the string representation does not match the
        expected format.
    """
    address = Address.objects.create(
        number="10",
        street="Downtown Street",
        city="London",
        state="UK",
        zip_code=12345,
        country_iso_code="GB",
    )
    assert str(address) == "10 Downtown Street"


def test_address_verbose_name():
    """
    Verify the verbose names defined for the Address model.
    This test ensure that the singular and plural verbose names are correct.

    Parameters:
        None
    Returns:
         None
    Raises:
        AssertionError: If the verbose names ar not correctly defined.
    """
    assert Address._meta.verbose_name == "Address"
    assert Address._meta.verbose_name_plural == "Addresses"


def test_letting_str_returns_title():
    """
    Verify that the string representation of a letting is readable.
    This test ensure that the Letting model return the expected string with
    the title.

    Parameters:
        None
    Returns:
        None
    Raises:
        AssertionError: If the string representation does not match the
        expected format.
    """
    address = Address.objects.create(
        number="10",
        street="Downtown Street",
        city="London",
        state="UK",
        zip_code=12345,
        country_iso_code="GB",
    )
    letting = Letting.objects.create(
        title="Cosy apartment",
        address=address,
    )
    assert str(letting) == "Cosy apartment"


def test_letting_verbose_name():
    """
    Verify the verbose names defined for the Letting model.
    This test ensure that the singular and plural verbose names are correct.

    Parameters:
        None
    Returns:
         None
    Raises:
        AssertionError: If the verbose names ar not correctly defined.
    """
    assert Letting._meta.verbose_name == "Letting"
    assert Letting._meta.verbose_name_plural == "Lettings"
