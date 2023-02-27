# Author: Lukas Halbritter <halbi93@gmx.de>
# Copyright 2023

# pylint: disable=missing-docstring
import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self._browser = webdriver.Firefox()

    def tearDown(self):
        self._browser.quit()

    def test_homepage_title_contains_project_name(self):
        self._browser.get("http://localhost:8000")
        self.assertIn("Pollux", self._browser.title)
