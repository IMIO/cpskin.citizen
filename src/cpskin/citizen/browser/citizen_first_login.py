# -*- coding: utf-8 -*-
from geopy.geocoders.osm import Nominatim
from geopy.geocoders.googlev3 import GoogleV3
from geopy.exc import GeocoderTimedOut

import geocoder
import logging
logger = logging.getLogger('cpskin.citizen get lat lon')


def create_lat_lon(event):
    user = event.object
    loc = get_lat_lon_from_address(
        user.street, user.number, user.zip_code, user.location)


def get_lat_lon_from_address(street, number, zip_code, city):
    location = None
    if street is not None and city is not None:
        address = "{} {} {} {}".format(
            number,
            street.encode('utf8'),
            zip_code,
            city.encode('utf8'))
        g = geocoder.google(address)
        if g:
            return g.latlng
        location = get_address(Nominatim(), address, 'OSM')
        if not location:
            location = get_address(GoogleV3(), address, 'Google')
        if not location:
            return
    return location


def get_address(geolocator, address, geolocator_name):
    try:
        location = geolocator.geocode(address)
    except GeocoderTimedOut:
        logger.error("{} timeout".format(geolocator_name))
        return False
    if not location:
        logger.error("{} didn't know this address '{}'".format(
            geolocator_name, address))
        return False
    return {'lat': location.latitude, 'lon': location.longitude}
