import json

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Education, Transport
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from myapp.analytics.data_analysis import renderdata, renderdata1
from designer.dForm import LayoutForm
from designer.models import Item, ItemBloc, TypeItem, Bloc, BlocEcran, Ecran, Modele
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import authenticate, login, logout, models


# Create your views here.

def login_request(request):
    user = request.user
    if user.is_authenticated and not user.is_anonymous:
        return redirect('transport')

    error_message = False
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('transport')

            error_message = True
        error_message = True
    form = AuthenticationForm()
    return render(request=request, template_name="login.html",
                  context={"form": form, 'ERROR_MESSAGE': error_message})


@login_required
def logout_request(request):
    logout(request)
    return redirect('transport')

def get_layout(modele):
    Modele.objects.filter()

@login_required
@permission_required('myapp.view_transport', raise_exception=True)
def transport(request):

    try:
        trans = Transport.objects.all().values()
        data = renderdata1(trans)

        mylayout = {
            1: {
                'card1': 'number',
                'card2': 'number',
                'card3': 'number'
            },
            2: {
                'card1': 'ColumnChart'
            },
            3: {
                'card1': 'BarChart',
            },
            4: {
                'card1': 'PieChart',
                'card2': 'Line'
            },
            5: {
                'card1': 'Table'
            }
        }
        jsonlayout = json.dumps(mylayout)


    except ObjectDoesNotExist:
        raise Http404("Object does not exist")

    return render(request, 'index.html', {
        'mydata': data, 'mylayout': jsonlayout, 'user': request.user, 'page_title': 'Ministère du transport'})


@login_required
@permission_required('myapp.view_education')
def education(request):

    try:
        edu = Education.objects.all().values()
        data = renderdata(edu)

        mylayout = {
            1: {
                'card1': 'number',
                'card2': 'number',
                'card3': 'number'
            },
            2: {
                'card1': 'ColumnChart'
            },
            3: {
                'card1': 'BarChart',
            },
            4: {
                'card1': 'PieChart',
                'card2': 'Line'
            },
            5: {
                'card1': 'Table'
            }
        }
        jsonlayout = json.dumps(mylayout)

    except ObjectDoesNotExist:
        raise Http404("Object does not exist")

    user = request.user
    return render(request, 'index.html', {'mydata': data, 'mylayout': jsonlayout,
                                          'page_title': "Ministère de l'education Nationale "})
