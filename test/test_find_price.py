from navigate_directory.find_price import EnterValid
from navigate_directory.find_price import HomePage
from navigate_directory.find_price import FindPrice


def test_search(coin, browser):

    HomePage(browser).navigate_to_search()

    EnterValid(browser).enter_valid_to_search(coin)

    return FindPrice(browser).find_price()
