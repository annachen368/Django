import random

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    excuses = [
        "Hello my name is Anna",
        "I'd like to join django",
        "It works on my machine",
        "Not today, thanks",
    ]

    # output = """
        # <!DOCTYPE HTML>
        # <html>
        # <head>
        #   <title>test</title>
        # </head>
        # <body>
        # hello
        # {excuse}
        # </body>
        # </html>

    # """.format(excuse=random.choice(excuses))
    
    # return HttpResponse(excuses[1].upper())
    # return HttpResponse(output)

    excuse = random.choice(excuses)
    return render(request, "index.html", {'excuse': excuse})
    
