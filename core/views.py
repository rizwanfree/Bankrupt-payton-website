from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from .forms import ContactForm
import string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def searchByName(request):
    names = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        names = Case.objects.filter(last_name__icontains=search).all()
    else:
        names = Case.objects.all()
    paginator = Paginator(names, 100)
    paginator.orphans = 5
    page = request.GET.get('page')

    try:
        names = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        names = paginator.page(1)
    except EmptyPage:
        names = paginator.page(paginator.num_pages)
    context = {
        'names': names
    }
    return render(request, 'core/byname.html', context)


def caseDetails(request, slug):
    name = get_object_or_404(Case, slug=slug)
    context = {
        'name': name
    }
    return render(request, 'core/case-detail.html', context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:        
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

# def stateList(request):
#     states = State.objects.all()

#     context = {
#         'states': states
#     }
#     return render(request, 'core/states.html', context)


def searchByState(request, sid):
    names = None
    names = Case.objects.filter(state=sid)
    # if request.GET.get('search'):
    #     search = request.GET.get('search')
    #     names.filter(name__icontains=search).all()
    # else:
    #     names = Case.objects.filter(state=sid)
    paginator = Paginator(names, 75)
    paginator.orphans = 4
    page = request.GET.get('page')
    try:
        names = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        names = paginator.page(1)
    except EmptyPage:
        names = paginator.page(paginator.num_pages)
    context = {
        'names': names
    }
    return render(request, 'core/bystate.html', context)
