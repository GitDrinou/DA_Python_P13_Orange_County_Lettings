from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represent an extended user profile.
    This model extends the Django's User model with additional profile
    information, such as the user's favorite city.

    Attributes:
        user (OneToOneField): the related Django user instance.
        favorite_city (CharField): the user's favorite city.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="new_profile"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Function that returns a readable string representation of the profile.

        Returns:
            str: the username of the related user.
        :return:
        """
        return self.user.username
