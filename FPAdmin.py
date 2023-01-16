import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="restaraunts"
)

def addRestaurant(name, adress):
    global mydb
    mycursor = mydb.cursor()

    sql = 'INSERT INTO restarants(id, name, adress) VALUES(null, %s, %s)'
    values = (name, adress)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteRestaurant(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "DELETE FROM restarants WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()

def updateRestaurant(id, name, adress):
    global mydb
    mycursor = mydb.cursor()
    sql = "UPDATE restarants SET name = %s, adress = %s WHERE id = " + str(id)
    values = (name, adress)
    mycursor.execute(sql, values)
    mydb.commit()

def getRestaurant():
    global mydb
    mycursor = mydb.cursor()
    sql = "SELECT * FROM restarants"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def addFoodType(name):
    global mydb
    mycursor = mydb.cursor()

    sql = "INSERT INTO food_types(id, name) VALUES (null, %s)"
    values = (name,)
    mycursor.execute(sql, values)
    mydb.commit()

def updateFoodType(id, name):
    global mydb
    mycursor = mydb.cursor()
    sql = "UPDATE food_types SET name = %s WHERE id = " + str(id)
    values = (name,2)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteFoodType(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "DELETE FROM food_types WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()

def getFoodType():
    global mydb
    mycursor = mydb.cursor()
    sql = "SELECT * FROM food_types"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def addFood(name, price, description, foodtype_id, restaurant_id):
    global mydb
    mycursor = mydb.cursor()

    sql = 'INSERT INTO foods(id, name, price, description, foodtype_id, restaurant_id) VALUES(null, %s, %s, %s, %s, %s)'
    values = (name, price, description, foodtype_id, restaurant_id)
    mycursor.execute(sql, values)
    mydb.commit()

def updateFood(id, name, price, description, foodtype_id, restaurant_id):
    global mydb
    mycursor = mydb.cursor()
    sql = "UPDATE foods SET name = %s, price = %s, description = %s, foodtype_id = %s, restaurant_id = %s WHERE id = " + str(id)
    values = (name, price, description, foodtype_id, restaurant_id)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteFood(id):
    global mydb
    mycursor = mydb.cursor()

    sql = "DELETE FROM foods WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()

def getFood():
    global mydb
    mycursor = mydb.cursor()
    sql = "SELECT * FROM foods"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

while True:
  print("PRESS 1 TO CHANGE RESTAURANTS")
  print("PRESS 2 TO CHANGE FOOD TYPE")
  print("PRESS 3 TO CHANGE FOODS")
  print("PRESS 0 TO EXIT")

  choice = input()

  if choice == '1':
      print("PRESS 1 TO ADD RESTAURANT")
      print("PRESS 2 TO DELETE RESTAURANT")
      print("PRESS 3 TO UPDATE RESTAURANT")
      print('PRESS 4 TO LIST RESTAURANTS')
      print("PRESS 0 TO EXIT")

      choice = input()

      if choice == "1":
          print("INSERT NAME:")
          name = input()
          print("INSERT ADRESS:")
          adress= input()
          addRestaurant(name, adress)

      elif choice == '2':
          restaurant = getRestaurant()
          for res in restaurant:
              print(res)

          print("CHOOSE ID OF RESTAURANT TO DELETE:")
          id = input()
          deleteRestaurant(id)

      elif choice == '3':
          restaurant = getRestaurant()
          for res in restaurant:
              print(res)

          print("CHOOSE ID OF RESTAURANT TO UPDATE:")
          id = input()

          print("INSERT NEW NAME:")
          name = input()
          print("INSERT NEW ADRESS:")
          adress = input()
          updateRestaurant(id, name, adress)

      elif choice == '4':
          restaurant = getRestaurant()
          for res in restaurant:
              print(res)

      elif choice == '0':
          break

  elif choice == '2':
      print("PRESS 1 TO ADD FOOD TYPE")
      print("PRESS 2 TO DELETE FOOD TYPE")
      print("PRESS 3 TO UPDATE FOOD TYPE")
      print('PRESS 4 TO LIST FOOD TYPE')
      print("PRESS 0 TO EXIT")

      choice = input()
      if choice == '1':
          print("INSERT NAME:")
          name = input()
          addFoodType(name)

      elif choice == '2':
          foodtype = getFoodType()
          for ft in foodtype:
              print(ft)

          print("CHOOSE ID OF FOODTYPE TO DELETE:")
          id = input()
          deleteFoodType(id)

      elif choice == '3':
          foodtype = getFoodType()
          for ft in foodtype:
              print(ft)

          print("CHOOSE ID OF FOOD TYPE TO UPDATE:")
          id = input()

          print("INSERT NEW NAME:")
          name = input()

          updateFoodType(id, name)

      elif choice == '4':
          foodtype = getFoodType()
          for ft in foodtype:
              print(ft)

      elif choice == '0':
          break

  elif choice == '3':
      print("PRESS 1 TO ADD FOOD")
      print("PRESS 2 TO DELETE FOOD")
      print("PRESS 3 TO UPDATE FOOD")
      print('PRESS 4 TO LIST FOOD')
      print("PRESS 0 TO EXIT")

      choice = input()

      if choice == '1':
          print("INSERT NAME:")
          name = input()
          print("INSERT PRICE:")
          price = input()
          print("INSERT DESCRIPTION:")
          description = input()
          print("INSERT FOODTYPE ID:")
          foodtype_id = input()
          print("INSERT RESTAURANT ID:")
          restaurant_id = input()
          addFood(name, price, description, foodtype_id, restaurant_id)

      elif choice == '2':
          food = getFood()
          for f in food:
              print(f)

          print("CHOOSE ID OF FOOD TO DELETE:")
          id = input()
          deleteFood(id)

      elif choice == '3':
          food = getFood()
          for f in food:
              print(f)

          print("CHOOSE ID OF FOOD TO UPDATE:")
          id = input()

          print("INSERT NEW NAME:")
          name = input()
          print("INSERT NEW PRICE:")
          price = input()
          print("INSERT NEW DESCRIPTION:")
          description = input()
          print("INSERT NEW FOODTYPE ID:")
          foodtype_id = input()
          print("INSERT NEW RESTAURANT ID:")
          restaurant_id = input()

          updateFood(id, name, price, description, foodtype_id, restaurant_id)

      elif choice == '4':
          food = getFood()
          for f in food:
              print(f)

      elif choice == '0':
          break

  elif choice == '0':
      break







