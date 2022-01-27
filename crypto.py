import os
from datetime import datetime
from selenium import webdriver
from test.test_find_price import test_search
from utils import convert_string_to_dict_from_file

create_file = os.path.exists("NewFile.txt")
current_datatime = datetime.now()
file = "NewFile.txt"

while True:
    print("Hello user! you can select one of these options: 1 - Add transaction,"
          " 2 - Get total balance, 3 - Sell coins, 4 - Average, 5 - Get earnings percent")

    options = int(input("choose a transaction: "))

    if options == 1:
        coin_title_input = input("text coin ticker: ").upper()
        full_ticker_name_input = input("text full name ticker: ")
        coin_amount_input = input("amount of tokens that were bought: ")
        price_input = input("price of the token: ")

        total_purchase_price = int(coin_amount_input) * int(price_input)

        new_dictionary = \
            {
                f"{coin_title_input}": {"time": current_datatime.strftime("%Y-%m-%d %H:%M"),
                                        "full_ticker_name": full_ticker_name_input,
                                        "coin_amount": coin_amount_input,
                                        "price": price_input,
                                        "total_balance": total_purchase_price}
            }

        my_file = open("NewFile.txt", "a")
        my_file.write(f"{new_dictionary}\n")
        my_file.close()

    elif options == 2:
        coin_title = input("text coin ticker: ").upper()
        my_file_1 = open("NewFile.txt", "r")
        readline = my_file_1.readlines()
        dict_with_second_options = convert_string_to_dict_from_file(readline)
        my_file_1.close()
        balance_top = 0
        total_balance = balance_top + int(dict_with_second_options[str(coin_title)]["total_balance"])

        print(f'Dear user, your total balance is {total_balance} $')

    elif options == 3:

        coin_title_for_sell = input("text coin ticker: ").upper()
        full_ticker_name_for_sell = input("text full name ticker: ")
        coin_amount_for_sell = input("amount of tokens that were bought: ")
        coin_price_for_sell = input("price of the token: ")

        my_file = open("NewFile.txt", "r")

        readlines = my_file.readlines()
        dict_with_coins = convert_string_to_dict_from_file(readlines)

        if int(dict_with_coins[str(coin_title_for_sell)]["coin_amount"]) < int(coin_amount_for_sell):

            print("Dear user, you have a mistake in amount!")

        else:

            next_file = open("NewFile.txt", "a")
            coin_amount_after_sell = \
                int(dict_with_coins[str(coin_title_for_sell)]["coin_amount"]) - int(coin_amount_for_sell)
            balance_coin = int(coin_price_for_sell) * int(coin_amount_for_sell)
            balance_after_sell = int(dict_with_coins[str(coin_title_for_sell)]["total_balance"]) - int(balance_coin)

            if coin_amount_after_sell == 0:
                balance_for_profit = str(balance_after_sell).replace("-", "")
                print(f"Your profit is {balance_for_profit}")
                my_file = open("NewFile.txt", "a")
                main_dictionary = \
                    {
                        f"{coin_title_for_sell}": {"time": current_datatime.strftime("%Y-%m-%d %H:%M"),
                                                   "full_ticker_name": full_ticker_name_for_sell,
                                                   "coin_amount": 0,
                                                   "price": 0,
                                                   "total_balance": balance_for_profit}
                    }

                my_file.write(f"{main_dictionary}\n")
                my_file.close()

            else:
                average_price = int(balance_after_sell) / int(coin_amount_after_sell)
                sell_dictionary = \
                    {
                        f"{coin_title_for_sell}": {"time": current_datatime.strftime("%Y-%m-%d %H:%M"),
                                                   "full_ticker_name": full_ticker_name_for_sell,
                                                   "coin_amount": coin_amount_after_sell,
                                                   "price": average_price,
                                                   "total_balance": balance_after_sell}
                    }

                next_file.write(f"{sell_dictionary}\n")
                next_file.close()

    elif options == 4:
        coin_title = input("text coin ticker: ").upper()
        full_ticker_name = input("text full name ticker: ")
        coin_amount = input("amount of tokens that were bought: ")
        average_price = input("price of the token: ")

        my_file = open("NewFile.txt", "r")
        readline = my_file.readlines()
        dict_with_coins = convert_string_to_dict_from_file(readline)

        my_file = open("NewFile.txt", "a")
        average_amount = int(coin_amount) + int(dict_with_coins[str(coin_title)]["coin_amount"])
        balance_after_average = int(coin_amount) * int(average_price)
        total_balance_after_average = \
            int(dict_with_coins[str(coin_title)]["total_balance"]) + int(balance_after_average)
        average_purchase_price = float(total_balance_after_average) / float(average_amount)

        average_dictionary = {
            f"{coin_title}": {
                "time": current_datatime.strftime("%Y-%m-%d %H:%M"),
                "full_ticker_name": full_ticker_name,
                "coin_amount": average_amount, "price": average_purchase_price,
                "total_balance": total_balance_after_average
            }
        }

        my_file.write(f"{average_dictionary}\n")
        my_file.close()

    elif options == 5:
        ticker_name_input = input("text ticker name: ").upper()
        full_name_ticker_input = input("text full name ticker: ")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://coinmarketcap.com/")

        coin_price = test_search(full_name_ticker_input, driver)

        driver.close()

        update_coin_element = coin_price.replace("$", "")
        # change dollar element to nothing

        my_file = open("NewFile.txt", "r")

        readline = my_file.readlines()
        dictionary = convert_string_to_dict_from_file(readline)

        earnings = float(dictionary[ticker_name_input]["coin_amount"]) * float(update_coin_element)
        total_earning_balance = float(earnings) - float(dictionary[ticker_name_input]["total_balance"])
        percent = float(total_earning_balance) / float(100)

        print(f"data time: {current_datatime.strftime('%Y-%m-%d %H:%M')} {ticker_name_input} gave: {percent} %\n")
        my_file.close()
