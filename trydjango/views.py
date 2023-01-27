from django.http import HttpResponse
import random


def home(request):
    
    
    name = 'halima'
    number = random.randint(10,89785)
    # from databses
    
    #django templates
    html_string =f"""
    <h1>hello {name} - {number}</h1>
    """
    
    p_string =f"""
    <p>hi {name} - {number}</p>
    """
    html_string = html_string+ p_string
    return HttpResponse(html_string)
