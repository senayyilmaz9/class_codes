from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class BasicSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_basic_selenium_project(self):

        self.driver.get("https://www.lcwaikiki.com/")


        category_link = self.driver.find_element_by_xpath("//@[class='category']")
        category_link.click()
        time.sleep(2)


        product_link = self.driver.find_element_by_xpath("//div[class='product']/")
        product_link.click()
        time.sleep(2)


        add_to_cart_button = self.driver.find_element_by_xpath("//button[id='add-to-cart']")
        add_to_cart_button.click()
        time.sleep(2)


        cart_link = self.driver.find_element_by_xpath("//[id='cart']")
        cart_link.click()
        time.sleep(2)


        home_link = self.driver.find_element_by_xpath("//[class='home']")
        home_link.click()
        time.sleep(2)


        self.assertTrue("Ana Sayfa" in self.driver.title)



if __name__ == "__main__":
    unittest.main()
