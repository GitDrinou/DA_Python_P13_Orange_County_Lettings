from django.shortcuts import render, get_object_or_404
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum
# id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Function that renders the lettings index page.
    This view retrieves all available letting records and provides access to
    the different sections of the application, such as home and profiles
    Parameters:
         request(HttpRequest): The incoming HTTP request.
    Returns:
        HTTPResponse: the rendered lettings index page containing the list
        of all lettings.
    Raises:
        Http404: If no letting exists for the given identifier.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean
# finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue,
# dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem
# accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac
# non tellus. In tristique mauris eu velit fermentum, tempus pharetra est
# luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non
# dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting_detail(request, letting_id):
    """
    Function that renders the detail page for a specific letting.
    This view retrieves a letting by its identifier and displays its title
    and address information. If no letting matches the provided identifier,
    a 404 error is raised.
    Parameters:
        request(HttpRequest): The incoming HTTP request.
        letting_id(int): The unique identifier of the letting to retrieve
    Returns:
        HttpResponse: the rendered  detail page for the selected letting.
    Raises:
        Http404: If no letting exists for the given identifier.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
