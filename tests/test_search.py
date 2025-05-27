from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_browser")
class TestSearch:


    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product             


    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        home_page.click_search_button()
        search_page = SearchPage(self.driver) 
        assert "no product that matches the search criteria" in search_page.display_status_of_invalid_product().lower()      


    def test_serch_without_any_product(self):
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        home_page.click_search_button()
        search_page = SearchPage(self.driver) 
        assert "no product that matches the search criteria" in search_page.display_status_of_invalid_product().lower() 
        

   

