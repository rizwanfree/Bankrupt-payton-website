import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Case
from blog.models import Post
#from .forms import ContactForm
import string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from contactforms.forms import ContactForm


# Create your views here.

state_dictionary = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


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
    filed_date = datetime.datetime.strptime(name.date_filed, "%m-%d-%Y")
    context = {
        'name': name,
        'filed_date': filed_date,
    }
    return render(request, 'core/case-detail.html', context)


def statePage(request):
    return render(request, 'core/states.html', {'states': state_dictionary})


def searchByState(request, sname):
    names = None
    names = Case.objects.filter(state=sname)
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
