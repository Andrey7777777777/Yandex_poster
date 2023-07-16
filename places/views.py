from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from places.models import Places
from django.urls import reverse


def places(request, place_id):
    place = get_object_or_404(Places, pk=place_id)
    detailsUrl = {"title": place.title,
                  'imgs': [image.image.url for image in place.images.all()],
                  'description_short': place.short_description,
                  'description_long': place.long_description,
                  'coordinates': {'lat': place.latitude,
                                  'lng': place.longitude
                                  }
                  }
    response = JsonResponse(detailsUrl,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False,
                                               'indent': 4})
    return response


def index(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": []}
    places = Places.objects.all()
    for place in places:
        places_geojson["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.latitude, place.longitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.place_id,
                    "detailsUrl": reverse('place', args=[place.id])
                }
            }
        )
    data = {'places_geojson': places_geojson}
    return render(request, "index.html", context=data)
