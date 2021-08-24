from django.shortcuts import render, HttpResponse, redirect
from django101.cities.models import Person



def index(req):
    context = {
        'name': 'MyName',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def create_person(req):
    Person(
        name='Pesho',
        age=18,
        home_town='Pernik'
    ).save()
    return redirect('/cities')

def test_index(req):
    return HttpResponse(
        '{"name": "Myname"}',
        content_type='text',
    )


def list_phones(req):
    context = {
        'phones': [
            {
                'name': 'Galaxy s500',
                'quantity': 3,
            },
            {
                'name': 'iPhone 12',
                'quantity': 4,
            },
            {
                'name': 'Xiaomy Redmi 5',
                'quantity': 0,
            },
        ]
    }

    context['message'] = 'Phones list'

    return render(req, 'phones.html', context)
