import pytest
from selenium import webdriver
from time import sleep

def test1(browser):
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
    sleep(30)