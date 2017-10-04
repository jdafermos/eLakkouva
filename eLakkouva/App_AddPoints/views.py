from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import GEOSGeometry
from .forms import thePitsForm, theBulbsForm, theLeaksForm
from .models import Pits, Bulbs, Leaks

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

def thePitsDatasetView(request):
    thePitFeatures = serialize('geojson', Pits.objects.all())
    return HttpResponse(thePitFeatures, content_type='json')

def theBulbsDatasetView(request):
    theBulbFeatures = serialize('geojson', Bulbs.objects.all())
    return HttpResponse(theBulbFeatures, content_type='json')

def theLeaksDatasetView(request):
    theLeakFeatures = serialize('geojson', Leaks.objects.all())
    return HttpResponse(theLeakFeatures, content_type='json')

def thePopupView(request):
    # If the form has been submitted
    if request.method == "POST":

        # Process the data in the cleaned_data
        theLonData = request.POST.get('p_field_lon', '')
        theLatData = request.POST.get('p_field_lat', '')
        theCommentData = request.POST.get('p_field_comment', '')
        theLayerSelection = request.POST.get('p_field_layer', '')

        # Make a form bound to the POST data
        thePopupModelForm = None
        if theLayerSelection == "layer_pits":
            thePopupModelForm = thePitsForm(request.POST)
        elif theLayerSelection == "layer_bulbs":
            thePopupModelForm = theBulbsForm(request.POST)
        elif theLayerSelection == "layer_leaks":
            thePopupModelForm = theLeaksForm(request.POST)

        # Make a new Point geometry object in WKT format
        thePoint = GEOSGeometry( 'POINT(' + str(theLonData) + ' ' + str(theLatData) + ')' )

        # All validation rules pass, therefore create a new object and add it to the database
        if thePopupModelForm.is_valid():
            if theLayerSelection == "layer_pits":
                thePitObject = Pits(Comment=theCommentData, Coords=thePoint)
                thePitObject.save()

            elif theLayerSelection == "layer_bulbs":
                theBulbObject = Bulbs(Comment=theCommentData, Coords=thePoint)
                theBulbObject.save()

            elif theLayerSelection == "layer_leaks":
                theLeakObject = Leaks(Comment=theCommentData, Coords=thePoint)
                theLeakObject.save()

            # Redirect to Home Page after POST
            return HttpResponseRedirect(reverse('theHomePageViewURL'))

        else:
            return HttpResponse("Form validation has failed")

    else:
        return HttpResponse("Request method is not POST")