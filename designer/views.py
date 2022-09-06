import json

from django.shortcuts import render
from django.http import HttpResponse
from designer.models import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from myapp.analytics.data_analysis import renderdata
from designer.dForm import LayoutForm
from .models import Item, ItemBloc, TypeItem, Bloc, BlocEcran, Ecran, Modele
from urllib import parse


# Create your views here.

def preview(request):
    render(request, 'blocForm.html', {'modele_data': {}})


def buildmodele(request):
    # create object of form
    if request.method == 'POST':
        formset = LayoutForm(request.POST, request.FILES)

        if formset.is_valid:

            layout = formset.data['layout_dict']
            modele_title = formset.data['modele_title']
            json_object = json.loads(layout)
            print(json_object)
            formset = LayoutForm()

            # Create modele Model and ecran Model to insert in Db
            modele_ = Modele(modele_libelle=modele_title)
            modele_.save()

            ecranlabel = 'ecran' + str(modele_.modele_id) + modele_title
            ecran_ = Ecran(modele_id=modele_.modele_id, ecran_libelle=ecranlabel)
            ecran_.save()

            y = 1
            # iterate through json object
            for bloc_keys, bloc_values in json_object.items():
                x = 1
                bloc_label = bloc_keys + '_' + ecranlabel

                # insert new bloc
                bloc_ = Bloc(bloc_libelle=bloc_label)
                bloc_.save()
                print('saved bloc', bloc_)

                # insert new Bloc Ecran
                blocecran_ = BlocEcran(ecran_id=ecran_.ecran_id, bloc_id=bloc_.bloc_id, x=0, y=y, h=0)
                blocecran_.save()

                y = y + 1
                # iterate through value of each dictionary in the json object
                for item_keys, item_values in bloc_values.items():

                    print('key = ', item_keys, '| value = ', item_values)

                    if item_values == 'number':  # get Item Type Ids
                        type_item_id = TypeItem.objects.values_list('type_item_id', flat=True).get(
                            type_item_libelle='Afficheur')
                    else:
                        type_item_id = TypeItem.objects.values_list('type_item_id', flat=True).get(
                            type_item_libelle='Graphique')

                    print('type item id :', type_item_id)
                    item_ = Item(type_item_id=type_item_id, item_libelle=item_values)
                    print('saved item', item_)
                    item_.save()

                    itembloc_ = ItemBloc(item_id=item_.item_id, bloc_id=bloc_.bloc_id, x=x, y=0, h=0)
                    itembloc_.save()
                    x = x + 1

            render(request, 'blocForm.html', {'formset': formset})

        # check if form data is valid
        # if formset.is_valid():
        #   formset.save()        # save the form data to model
        #  statut = 'successful'
    else:
        formset = LayoutForm()

    return render(request, 'blocForm.html', {'formset': formset})