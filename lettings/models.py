from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represent a postal address associated with a letting.
    This model stores the different components of a physical address,
    with street number, street name, city, state, zip code, and country
    ISO code.

    Attributes:
        number (PositiveIntegerField): the street number
        street (CharField): the street name
        city (CharField): the city name
        state (CharField): the 2 character state code
        zip_code (PositiveIntegerField): the zip or postal code
        country_iso_code (CharField): The 3 character ISO country code
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Function that returns a readable string representation of the address.

        Returns:
            str: the street number following by the street name
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represent a rental letting.
    This model stores the title of the letting and links it to a unique
    address.

    Attributes:
        title (CharField): the title of the letting
        address (OneToOneField): the address associated with the letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Function that returns a readable string representation of the letting..

        Returns:
            str: the title of the letting
        """
        return self.title
