from navigate_directory.find_price import EnterValid
from navigate_directory.find_price import FindPrice
from navigate_directory.find_price import HomePage


def test_search(coin, browser):
    HomePage(browser).navigate_to_search()

    EnterValid(browser).enter_valid_to_search(coin["coin_ticker"])

    price = FindPrice(browser).find_price()
    print(price.text)
