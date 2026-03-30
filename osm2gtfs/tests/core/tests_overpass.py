# coding=utf-8

import os
import unittest

from mock import patch

from osm2gtfs.core.overpass import (
    DEFAULT_OVERPASS_URL,
    OVERPASS_URL_ENV_VAR,
    get_overpass_api,
    get_overpass_url,
)


class TestOverpassConfiguration(unittest.TestCase):

    def test_default_overpass_url(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(get_overpass_url(), DEFAULT_OVERPASS_URL)

    def test_env_override_overpass_url(self):
        custom_url = "https://example.test/api/interpreter"
        with patch.dict(os.environ, {OVERPASS_URL_ENV_VAR: custom_url}, clear=True):
            self.assertEqual(get_overpass_url(), custom_url)
            self.assertEqual(get_overpass_api().url, custom_url)


if __name__ == '__main__':
    unittest.main()
