from django.http import HttpResponse


# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def primera(request):
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("arturito")