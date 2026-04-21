from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum,
# nulla eget feugiat sagittis, sem mi convallis eros, vitae dapibus nisi
# lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
# non finibus neque cursus id.
def index(request):
    """
    Function that renders the home page of the application.
    This view displays the main landing page and provides access to the
    different sections of the application, such as lettings and profiles.
    Parameters:
         request(HttpRequest): The incoming HTTP request.
    Returns:
        HTTPResponse: the rendered home page response
    """
    return render(request, 'index.html')
