from django.shortcuts import render


def index(req):
    context = {
        'name': 'MyName',
    }
    return render(req, 'index.html', context)
