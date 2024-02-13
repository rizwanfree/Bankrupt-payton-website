from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from blog.models import Post
from .forms import ContactForm
import string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def index(request):
    posts = Post.published.all().order_by('-id')[:4]
    posts1 = posts[:2]
    posts2 = posts[2:]
    print(len(posts2))
    context = {
        'posts1': posts1,
        'posts2': posts2
    }
    return render(request, 'core/index.html', context)


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


def contact_us(request):
    form = ContactForm()
    context = {'form': form}
    if request.method == 'POST':        
        form = ContactForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return render(request, 'core/contact.html', context)
            #return redirect('core:index')
        else:
            return render(request, 'core/contact.html', context)
    return render(request, 'core/contact.html', context)
    


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
