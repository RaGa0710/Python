from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.HomePage import HomePage
from pages.BasePage import BasePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):


    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        assert search_page.display_status_of_valid_product             


    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Honda")
        assert "no product that matches the search criteria" in search_page.display_status_of_invalid_product().lower()      


    def test_serch_without_any_product(self):
        home_page=HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        assert "no product that matches the search criteria" in search_page.display_status_of_invalid_product().lower() 
        

   

