# coding=utf-8

import os

import overpy

#DEFAULT_OVERPASS_URL = "https://overpass-api.de/api/interpreter"
DEFAULT_OVERPASS_URL = "https://ethiopia.overpass.openplaceguide.org/api/interpreter"
OVERPASS_URL_ENV_VAR = "OSM2GTFS_OVERPASS_URL"


def get_overpass_url():
    """Return the configured Overpass endpoint."""
    return os.environ.get(OVERPASS_URL_ENV_VAR, DEFAULT_OVERPASS_URL).strip() or DEFAULT_OVERPASS_URL


def get_overpass_api():
    """Create an Overpass client using the shared endpoint configuration."""
    return overpy.Overpass(url=get_overpass_url())
