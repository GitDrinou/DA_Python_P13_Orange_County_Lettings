import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile


logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor
# pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Function that renders the profiles index page.
    This view retrieves all user profiles and provides access to
    the different sections of the application, such as home and lettings

    Parameters:
         request(HttpRequest): The incoming HTTP request.
    Returns:
        HTTPResponse: the rendered profiles index page containing the list
        of all profiles.
    Raises:
        Http404: if the requested profile does not exist.
    """
    logger.info("Profile index page requested")

    try:
        profiles_list = Profile.objects.all()
        logger.info("Retrieved %s profiles", profiles_list.count())
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception:
        logger.exception("Unexpected error while loading profiles index page")
        raise


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males
def profile_detail(request, username):
    """
    Function that renders the detail page for a specific profile.
    This view retrieves a profile associated with the given username and
    displays its information. If not matching profile is found, a 404 error
    is raised.

    Parameters:
        request(HttpRequest): The incoming HTTP request.
        username(str): The username associated with the profile retrieve.
    Returns:
        HttpResponse: the rendered detail page for the selected profile.
    Raises:
        Http404: If no profile exists for the given username.
    """
    logger.info("Profile detail page requested for username=%s", username)

    if not username or not username.strip():
        logger.warning("Invalid username received: %s", username)

    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info("Profile found for username=%s", username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Http404:
        logger.warning("Profile not found for username=%s", username)
        raise
    except Exception:
        logger.exception("Unexpected error while loading profile detail for "
                         "username=%s", username)
        raise
