import os
from datetime import datetime
from utils import convert_string_to_dict_from_file

# Вот что тебе нужно сделать:
# 1 - While True цикл, пока для 1 опции это указать твою транзацкию, как это можно сделать:
# спрашивает выбери опцию, пишешь add transaction, после этого оно должно обработать что ты передал add transaction
# и дальше высрать для того что б добавить транзакцию - дай мне тикер и общую сумму на скок ты купил

# тикер и общую сумму отловить и его закинуть в файл, то есть что б было в файле то, что ты передашь в инпут
# вот твоя задача на сейчас ! ! !
# на другое не отвлекайся пока

# хочу что б ты добавить пока с помощью такого способа 3 монеты

# ------------------------------------------------ ЗАДАЧА 2 ----------------------------------------------
# Новые указания:
# добавить новую опцию(то есть принимать в инпут и по ифу фильтровать) какая будет называться - Get total balance.
# Как она будет работать: ты внизу апдейтнешь то, что человек указывает что б добавить транзакцию свою, а значение где
# (сколько монет умножить на цену) к ней вплотную присобачить символ доллара $
# что это даст нам:
# Когда юзер указывает get total balance, тебе нужно открыть файл, прочитать все линии и достать значение
# (ПЕРЕД ЗНАКОМ ДОЛЛАРА $ и до первого пробела!!!)
# например:

# DOT bought: 20, price: 25, total: 500$, вот тебе нужно вытянуть 500 ровно, для этого тебе нужны Python reg ex,
# нужно гуглить, типа лвлва - python regex get value between symbol and whitespace.)
# **** НО! тебе нужно это делать в цикле, где ты будешь перебирать каждую строку,
# и собирать и приплюсовывать все значения
# с total баланса, и в конечном итоге выплюнуть юзеру общую сумму его транзакций, то есть:

# DOT bought: 20, price: x, total: 500$
# DOT bought: 20, price: x, total: 600$
# DOT bought: 20, price: x, total: 1500$

# тебе нужно итерироваться по каждой строке и сделать - 500
# 500 + 600 = 1100
# 1100 + 1500 = 2600 и когда закончилась вся итерация выплюнуть юзеру вот твой тотал баланс : 2600

# если ты хочешь выполнить данное задание на звездочку капитана америки (типа бонусное задание)
# При добавлении записи в файл, найти либку с датой и временем и так же когда ты
# делаешь add transaction первым значением
# добавлять текущую дату и потом уже тикер, так же можно разделять таким знаком |
# пример что ты должен получать в файле:

# 20.12.2021 16:35 | DOT | bought: 20| price: 25| total: 500$


'''
    ___________________________________________________________________ЗАДАЧА 3__________________________________
    Новая таска - это нужно сменить местами, что б передавать не текстом get total balance и другие опции а
    отправлять цифру
    1 - это добавить транзакцию, 2- баланс, 3 -убавить ( над какой ты и будешь сегодня работать)
    Как она должна работать : Примерно так же принимать тикер и кол-во монет как и в add transaction, но!
    Тебе нужно как-то хендлить такие штуки как: 1)Что делать если ты передаешь тикер а такого у тебя вообще нету в файле
    2) Если ты хочешь удалить больше монет чем у тебя есть, например пишешь хочу удалить 100 монет а у тебя всего
    в файле 20
    3) Тебе нужно делать пересчёт, если у тебя было дот монета 20 штук по 25 баксов и тотал сумма 500, то тебе при 3 
    опции
    (продажа монеты), нужно: ты например передаешь что дота продал 10 штук по 30 баксов, то:
    тебе нужно 20 - 10 = 10 переписать количество монет в файле и взять тотал сумму 500 - (10*30) = 200  и перезаписать 
    файл
    ( я думаю это можно делать типа итерируешься по строкам файла, когда находишь в строке такой же тикер как ты передал
    в
    убавить транзакцию - (DOT / DOT ) начинаешь работать с тем лайном, оттуда получаешь всю инфу про сколько монет/цена
    и тд
    Дальше делаешь всю магию
    4 ) ТАК ЖЕ нужно перебрать способ добавления, ведь таким образом ты можешь заспавнить 10 записей в файл с одним
     DOTом
    То тебе нужно так же смотреть, а есть ли уже такой тикер в файле? если есть - прибавляешь и меняешь количество 
    монет и
    тотал сумму покупки, возможно подумать над тем, что не стоит хранить сумму за какую ты купил монету, а её сменить
    на среднюю
    сумму покупки, можно путем - ( total sum / amount of tokens)

'''
create_file = os.path.exists("NewFile.txt")
current_datatime = datetime.now()
file = "NewFile.txt"
while True:
    print("Hello user! you can select one of these options: 1 - Add transaction,"
          " 2 - Get total balance, 3 - Sell coins, 4 - Average, 5 - ")

    options = int(input("choose a transaction: "))

    if options == 1:
        coin_title_input = input("text coin ticker: ")
        full_ticker_name_input = input("text full name ticker: ")
        coin_amount_input = input("amount of tokens that were bought: ")
        price_input = input("price of the token: ")

        total_purchase_price = int(coin_amount_input) * int(price_input)

        new_dictionary = \
            {"time": current_datatime.strftime("%Y-%m-%d %H:%M"), "full_ticker_name": full_ticker_name_input,
             "coin_title": coin_title_input,
             "coin_amount": coin_amount_input,
             "price": price_input,
             "total_balance": total_purchase_price
             }

        my_file = open("NewFile.txt", "a+")
        my_file.write(str(new_dictionary) + "\n")
        my_file.close()

    elif options == 2:
        my_file_1 = open("NewFile.txt", "r")
        readline = my_file_1.readlines()
        dict_with_second_options = convert_string_to_dict_from_file(readline)
        my_file_1.close()
        balance_top = 0
        total_balance = balance_top + int(dict_with_second_options["total_balance"])

        print(f'Dear user, your total balance is {total_balance} $')

    elif options == 3:

        # coin_title = input("text coin ticker: ")
        # full_ticker_name = input("text full name ticker: ")
        # coin_amount = input("amount of tokens that were bought: ")
        # coin_price = input("price of the token: ")
        my_file = open("NewFile.txt", "r")
        readlines = my_file.readlines()
        print(readlines)
        dict_with_coins = convert_string_to_dict_from_file(readlines)
        print(dict_with_coins)

        # if dict_with_coins["coin_amount"] <= coin_amount:
        #     print("Dear user, you must correct your coin amount!")
        #
        # elif dict_with_coins["coin_title"] == coin_title:
        #     next_file = open("NewFile.txt", "a+")
        #     coin_amount_after_sell = int(dict_with_coins["coin_amount"]) - int(coin_amount)
        #     balance_coin = int(coin_price) * int(coin_amount)
        #     balance_after_sell = int(dict_with_coins["total_balance"]) - int(balance_coin)
        #     average_price = float(balance_after_sell) / float(coin_amount_after_sell)
        #     sell_dictionary = {"time": current_datatime.strftime("%Y-%m-%d %H:%M"),
        #                        "full_ticker_name": full_ticker_name,
        #                        "coin_title": coin_title, "coin_amount": coin_amount_after_sell,
        #                        "price": average_price, "total_balance": balance_after_sell
        #                        }
        #     next_file.write(str(sell_dictionary) + "\n")
        #     next_file.close()

    elif options == 4:
        coin_title = input("text coin ticker: ")
        full_ticker_name = input("text full name ticker: ")
        coin_amount = input("amount of tokens that were bought: ")
        average_price = input("price of the token: ")
        my_file = open("NewFile.txt", "r+")
        readline = my_file.readlines()
        dict_with_coins = convert_string_to_dict_from_file(readline)

        if dict_with_coins["coin_title"] == coin_title:
            my_file = open("NewFile.txt", "w+")
            average_amount = int(coin_amount) + int(dict_with_coins["coin_amount"])
            balance_after_average = int(coin_amount) * int(average_price)
            total_balance_after_average = int(dict_with_coins["total_balance"]) + int(balance_after_average)
            average_purchase_price = float(total_balance_after_average) / float(average_amount)
            average_dictionary = {"time": current_datatime.strftime("%Y-%m-%d %H:%M"),
                                  "full_ticker_name": full_ticker_name,
                                  "coin_title": coin_title,
                                  "coin_amount": average_amount, "price": average_purchase_price,
                                  "total_balance": total_balance_after_average}
            my_file.write(str(average_dictionary) + "\n")
            my_file.close()

    elif options == 5:
        coin_title = input("text coin ticker: ")
