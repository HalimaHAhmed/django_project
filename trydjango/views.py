from django.http import HttpResponse


def home(request):
    html_string = "<h1> hello halima</h1>"
    return HttpResponse(html_string)
