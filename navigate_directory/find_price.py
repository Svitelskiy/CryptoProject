from selenium.webdriver import Keys
from locators.search_locator import PriceLocators
from locators.search_locator import HomePageLocators


class HomePage:
    def __init__(self, browser):
        self.browser = browser

        self.button_search = self.browser.find_element(*HomePageLocators.search_button)

    def navigate_to_search(self):
        self.button_search.click()


class EnterValid:
    def __init__(self, browser):
        self.browser = browser

        self.input_search = self.browser.find_element(*HomePageLocators.search_input)

    def enter_valid_to_search(self, coin):
        self.input_search.send_keys(coin)
        self.input_search.send_keys(Keys.ENTER)


class FindPrice:
    def __init__(self, browser):
        self.browser = browser

    def find_price(self):
        coin_price = self.browser.find_element(*PriceLocators.price_value).text
        print(f"coin price is: {coin_price}")
        return coin_price
