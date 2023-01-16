import telebot

token = '1738155015:AAHyhnO8lKiYbHGAtsZgUJKPTwTR8gvYG0s'
bot = telebot.TeleBot(token)

import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="restaraunts"
)

def getAllFoodTypes():
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT * FROM food_types"
 mycursor.execute(sql)
 result = mycursor.fetchall()

 return result

def getAllRestaurants():
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT * FROM restarants"
 mycursor.execute(sql)
 result = mycursor.fetchall()

 return result

def getFoodsByRestaurantId(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restarantsName " \
          "FROM foods f " \
          "LEFT OUTER JOIN food_types ft ON ft.id = f.foodtype_id " \
          "LEFT OUTER JOIN restarants r ON r.id = f.restaurant_id " \
          "WHERE f.restaurant_id = "+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def getFoodByFoodType(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restarantsName " \
    "FROM foods f " \
    "LEFT OUTER JOIN food_types ft ON ft.id = f.foodtype_id " \
    "LEFT OUTER JOIN restarants r ON r.id = f.restaurant_id " \
    "WHERE f.foodtype_id = "+str(id)

    mycursor.execute(sql)
    result = mycursor.fetchall()

    return result

def getFood(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restarantsName " \
    "FROM foods f " \
    "LEFT OUTER JOIN food_types ft ON ft.id = f.foodtype_id " \
    "LEFT OUTER JOIN restarants r ON r.id = f.restaurant_id " \
    "WHERE f.id = "+str(id)

    mycursor.execute(sql)
    result = mycursor.fetchone()

    return result


def addtoBasket(user_id, food_id, count, price):
    global mydb
    mycursor = mydb.cursor()

    sql = 'INSERT INTO basket(id, user_id, food_id, count, price) VALUES (null, %s, %s, %s, %s) on duplicate key update count = count + 1, price = price * count '
    values = (user_id, food_id, count, price)
    mycursor.execute(sql, values)
    mydb.commit()

def getBasket(user_id):
    global mydb
    mycursor = mydb.cursor()

    sql = "SELECT f.name, b.count, b.price" \
          " FROM basket b" \
          " LEFT OUTER JOIN foods f ON f.id = b.food_id" \
          " WHERE b.user_id = " +str(user_id)

    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def deleteBasket(user_id):

    global mydb
    mycursor = mydb.cursor()

    sql = 'DELETE FROM basket WHERE user_id = ' +str(user_id)
    mycursor.execute(sql)
    mydb.commit()

menu = "main"

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global menu

    if message.text.lower() == "/start":
        text = ""
        text = text + "#########################\n"
        text = text + "Welcome to the food delivery service########################\n"
        text = text + "Choose an option below\n"
        text = text + "1 - Choose by type of food\n"
        text = text + "2 - Choose by restaurant\n"

        bot.send_message(message.chat.id, text)
        menu = "main"

    else:
        if menu == "main":
            if message.text.lower() == "1":
                allFoodTypes = getAllFoodTypes()
                text = "#####################\n"
                for food in allFoodTypes:
                    text = text + str(food[0]) + ") " + food[1] + "\n"
                menu = "choose_by_food_type"
                bot.send_message(message.chat.id, text)

            elif message.text.lower() == '2':
                allRestaurants = getAllRestaurants()
                text = "#####################\n"
                for rest in allRestaurants:
                    text = text + str(rest[0]) + ") " + rest[1] + "\n"
                menu = "choose_by_restaurant"
                bot.send_message(message.chat.id, text)

        elif menu == "choose_by_food_type":

            menu = "choose_food"

            id = message.text.lower()
            foods = getFoodByFoodType(id)
            text = "#####################\n"
            for food in foods:
                text = text + str(food[0]) + ") " + food[1] + " " + str(food[2]) + " KZT - " + food[7] + "\n"

            bot.send_message(message.chat.id, text)

        elif menu == "choose_by_restaurant":

            menu = "choose_food"
            id = message.text.lower()
            foods = getFoodsByRestaurantId(id)
            text = "#####################\n"
            for food in foods:
                text = text + str(food[0]) + ") " + food[1] + " " + str(food[2]) + " KZT - " + food[6] + "\n"
            bot.send_message(message.chat.id, text)


        elif menu == "choose_food":
            id = message.text.lower()
            food = getFood(id)

            user_id = message.from_user.id
            food_id = food[0]
            count = 1
            price = food[2]*count

            basket = addtoBasket(user_id, food_id, count, price)

            text = "You ordered " + food[1] + " for " + str(food[2]) + " KZT\n"
            text = text + "Contains: [" + food[3] + "] \n"
            text = text + 'Your order was succesfully added'
            bot.send_message(message.chat.id, text)

            text = ""
            text = text + 'Do you want to order anything else?\n'
            text = text + '1-yes\n'
            text = text + '2-no\n'
            menu = 'choose_number'
            bot.send_message(message.chat.id, text)

        elif menu == "choose_number":
            if message.text.lower() == '1':
                text = ''
                text = text + "Choose an option below\n"
                text = text + "1 - Choose by type of food\n"
                text = text + "2 - Choose by restaurant\n"
                bot.send_message(message.chat.id, text)
                menu = 'main'

            elif message.text.lower() == '2':

                user_id = message.from_user.id
                food = getBasket(user_id)
                totalprice = 0

                for f in food:
                    text = ''
                    text = 'your order was succesfully added \n'
                    text = "You ordered " + str(f[0]) + ' (quantity: ' + str(f[1]) + ')' + ' за ' + str(f[2]) + " KZT\n"
                    bot.send_message(message.chat.id, text)
                for f in food:
                    totalprice += f[2]
                text = ''
                text = text + "To be paid: " + str(totalprice) + 'KZT\n'
                text = text + "Thanks for your order\n"
                bot.send_message(message.chat.id, text)
                deleteBasket(user_id)


bot.polling(none_stop=True, interval=0)
