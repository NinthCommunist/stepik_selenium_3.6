import pytest
from selenium import webdriver

def test1(browser):
    browser.find_element_by_css_selector(".btn-add-to-basket")