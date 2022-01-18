from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class HomePageLocators:
    search_button = (By.XPATH, "//div[@class='sc-266vnq-0 fmdlWD']")
    search_input = (By.XPATH, "//input[@class='bzyaeu-3 jUraic']")


@dataclass
class PriceLocators:
    price_value = (By.CSS_SELECTOR, ".priceValue > span")
