from django.shortcuts import render
from places.models import Places


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
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            })

    data = {'places_geojson': places_geojson}
    return render(request, "index.html", context=data)
