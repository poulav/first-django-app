from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def allmembers(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'allmembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))


def test(request):
    member = Member.objects.values_list('firstname')
    template = loader.get_template('template.html')
    # context = Member.objects.all().values()
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))
