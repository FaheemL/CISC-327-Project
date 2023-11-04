import pyodbc
import database_initialization
from datetime import datetime

connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:cisc327-server.database.windows.net,1433;Database=db;Uid=CloudSAe60b9174;Pwd=Password123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

try:
    # Connect to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Check if the connection was successful
    print("Connected to the database!")

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error:", str(e))

"""
This class is used to define the methods that will information regarding the user and
their order(s) into the database.
"""


class DatabaseManager:
    # Creates connection to database
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = pyodbc.connect(connection_string)
        self.cursor = conn.cursor()

    # Saves user details in the database during account creation
    def save_user_details(self, user_id, user_name, user_email, user_password, user_address, user_phone, user_dropoff):
        insert_sql = "INSERT INTO Users (user_id, user_name, user_email, user_password, user_address, user_phone, user_dropoff) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(insert_sql, user_id, user_name, user_email,
                            user_password, user_address, user_phone, user_dropoff)
        self.conn.commit()

    # Allows user to update the user details in the database
    def update_user_details(self, user_id, user_name, user_email, user_password, user_address, user_phone, user_dropoff):
        update_sql = """
    UPDATE Users 
    SET user_name = ?, 
        user_email = ?,
        user_password = ?, 
        user_address = ?,
        user_phone = ?,
        user_dropoff= ? 
    WHERE user_id = ?
    """
        self.cursor.execute(update_sql, user_name, user_email, user_password,
                            user_address, user_phone, user_dropoff, user_id)
        self.conn.commit()

    # Allows the deletion of an account off the database
    def delete_user_details(self, user_id):
        delete_sql = "DELETE FROM Users WHERE user_id = ?"
        self.cursor.execute(delete_sql, user_id)
        self.conn.commit()

    # Saves payment method into database for a user
    def save_payment(self, payment_id, user_id, payment_method):
        insert_sql = "INSERT INTO PaymentMethods (payment_id, user_id, payment_method) VALUES (?, ?, ?)"
        self.cursor.execute(insert_sql, payment_id, user_id, payment_method)
        self.conn.commit()

    # Allows user to update payment information in the database
    def update_payment_details(self, payment_id, payment_method):
        update_sql = """
    UPDATE PaymentMethods 
    SET payment_method = ?
    WHERE payment_id = ?
    """
        self.cursor.execute(update_sql, payment_method, payment_id)
        self.conn.commit()

    # Allows the deletion of payment methods in the database
    def delete_payment(self, payment_id):
        delete_sql = "DELETE FROM PaymentMethods WHERE payment_id = ?"
        self.cursor.execute(delete_sql, payment_id)
        self.conn.commit()

    # Adds restaurant to database
    def add_restaurant(self, restaurant_id, name, cuisine, rating):
        insert_sql = "INSERT INTO Restaurants (restaurant_id, name, cuisine, rating) VALUES (?, ?, ?, ?)"
        self.cursor.execute(insert_sql, restaurant_id, name, cuisine, rating)
        self.conn.commit()

    # Updates restaurant information in database
    def update_restaurant_details(self, restaurant_id, name, cuisine, rating):
        update_sql = """
    UPDATE Restaurants
    SET name = ?,
        cuisine = ?,
        rating = ?
    WHERE restaurant_id = ?
    """
        self.cursor.execute(update_sql, name, cuisine, rating, restaurant_id)
        self.conn.commit()

    # Deletes a restaurant off the database
    def delete_restaurant(self, restaurant_id):
        delete_sql = "DELETE FROM Restaurants WHERE restaurant_id = ?"
        self.cursor.execute(delete_sql, restaurant_id)
        self.conn.commit()

    # Adds an item to a restaurant's menu in the database
    def add_menu_items(self, item_id, restaurant_id, name, price, options):
        insert_sql = "INSERT INTO MenuItems (item_id, restaurant_id, name, price, options) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(insert_sql, item_id,
                            restaurant_id, name, price, options)
        self.conn.commit()

    # Updates an item to a restaurant's menu in the database
    def update_menu_items(self, item_id, name, price, options):
        update_sql = """
    UPDATE MenuItems
    SET name = ?,
        price = ?,
        options = ?
    WHERE item_id = ?
    """
        self.cursor.execute(update_sql, name, price, options, item_id)
        self.conn.commit()

    # Deletes an item to a restaurant's menu in the database
    def delete_menu_items(self, item_id):
        delete_sql = "DELETE FROM MenuItems WHERE item_id = ?"
        self.cursor.execute(delete_sql, item_id)
        self.conn.commit()

    # Saves order details to the database
    def save_order(self, order_id, user_id, restaurant_id, total, status, order_time, order_details_id, item_id, quantity):
        insert_sql = "INSERT INTO Orders (order_id, user_id, restaurant_id, total, status, order_time) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(insert_sql, order_id, user_id,
                            restaurant_id, total, status, order_time)
        self.conn.commit()

        insert_sql = "INSERT INTO OrderDetails (order_details_id, order_id, item_id, quantity) VALUES (?, ?, ?, ?)"
        self.cursor.execute(insert_sql, order_details_id,
                            order_id, item_id, quantity)
        self.conn.commit()

    # Updates order status within the database
    def update_order(self, order_id, status):
        update_sql = """
    UPDATE Orders
    SET status = ?,
    WHERE order_id = ?
    """
        self.cursor.execute(update_sql, status, order_id)
        self.conn.commit()

    # Allows the deletion/cancellation of an order off the database
    def cancel_order(self, order_id):
        delete_sql = "DELETE FROM Orders WHERE order_id = ?"
        self.cursor.execute(delete_sql, order_id)
        self.conn.commit()

        delete_sql = "DELETE FROM OrderDEtails WHERE order_id = ?"
        self.cursor.execute(delete_sql, order_id)
        self.conn.commit()

    def save_review(self, review_id, order_id, user_id, review, rating, review_time):
        insert_sql = "INSERT INTO Reviews (review_id, order_id, user_id, review, rating, review_time) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(insert_sql, review_id, order_id,
                            user_id, review, rating, review_time)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


"""
This class is used to define a user's account details and allows them to login to their 
account, and potentially change account details.
"""


class Account:
    # The account is initialized as blank
    def __init__(self):
        self.user_name = None
        self.user_email = None
        self.user_id = None
        self.user_password = None
        self.user_address = None
        self.user_phone = None
        self.user_dropoff = None
        self.user_main_payment = None
        self.user_payment_methods = []

    def account_creation(self):
        """
        Function that creates a new account for users with information such as their name, 
        user ID, email, address, phone number, password, payment method, and dropoff 
        location.
        """

        print("Please enter the following information to create your account: ")

        self.user_name = input("Enter your name:")
        self.user_id = input("Enter your user ID:")
        self.user_email = input("Enter your email:")
        self.user_password = input("Enter your password:")
        self.user_address = input("Enter your address:")
        self.user_phone = input("Enter your phone number:")
        # Enter your main payment method which can be one of many methods
        self.user_main_payment = input("Enter your payment method:")
        self.user_payment_methods.append(self.user_main_payment)
        self.user_dropoff = input("Enter your preferred dropoff location:")

    def login(self):
        """
        Function that allows users to enter their user ID and password to be able to access 
        their account. 
        """

        print("Please enter your user ID and password to login to your account")

        user_id = input("Enter your user ID:")
        user_password = input("Enter your password:")

        if len(user_id) and len(user_password) != 0:
            print("Successful Login!")
        else:
            print("Login Failed. Please Try Again.")

    def account_management(self):
        """
        Function that allows users to edit account details such as their address, 
        phone number, password, payment method(s), and preferred drop off method. 
        """

        print("Please enter changes to the following information or press enter to skip:")

        self.user_password = input("Enter your password:")
        self.user_address = input("Enter your address:")
        self.user_phone = input("Enter your phone number:")
        # Change your payment method or add a new one
        self.user_main_payment = input("Enter your payment method:")
        if self.user_main_payment not in self.user_payment_methods:
            self.user_payment_methods.append(self.user_main_payment)
        self.user_dropoff = input("Enter your preferred dropoff location:")

        print("All changes successful!")


"""
This class defines a restaurant object with important details regarding a restaurant like 
the name, cuisine and rating.
"""


class Restaurant:
    # Constructor to make a restaurant
    def __init__(self, name, cuisine, rating):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating


"""
This class defines how users search for a restaurant from a list.
"""


class RestaurantView:
    # Constructor that creates a list of restaurants
    def __init__(self, restaurants):
        self.restaurants = restaurants

    def find_restaurant(self):
        """
        Function that allows users to search for a restaurant by name, cuisine, and/or 
        rating.
        """

        # This is a flag to check if results show up based on search criteria
        results_exist = False

        search_term = input("Search:")
        rating = input("Rating Filter:")
        cuisine = input("Cuisine Filter:")

        for restaurant in self.restaurants:
            if search_term in restaurant.name.lower() and \
               cuisine.lower() == restaurant.cuisine.lower() and \
               rating <= restaurant.rating:

                print(
                    f"{restaurant.name}\n {restaurant.cuisine} cuisine\n {restaurant.rating} stars")
                results_exist = True

        if not results_exist:
            print("No Results Found")


"""
This class defines an item in a restaurant's menu with important details such as name, 
price, and options. 
"""


class MenuItem:
    def __init__(self, name, price, options):
        self.name = name
        self.price = price
        self.quantity = 0
        self.options = options


"""
This class defines the mechanism to search through a restaurant's menu and select items 
to add to the cart, order, keep track of the order, rate it after it's delivered, and 
review any orders made in the past.
"""


class Order:
    def __init__(self, restaurant, items, past_orders):
        self.items = items
        self.cart = []
        self.order_details = {"restaurant": restaurant}
        self.progress = None
        self.past_orders = past_orders
        self.reviewed = False

    def add_menu_item(self):
        """
        Function that allows users to add items to their cart.
        """

        menu_item = input("Add Menu Item:")
        options = input("Select Options:")
        quantity = input("Quantity:")

        for item in self.items:
            if menu_item.lower == item.name.lower:
                item.quantity += quantity
                item.options = options
                self.cart.append(item)
                print(f"{item.name} added to cart")
                # Once the item is found no need to check others
                break

    def view_cart(self):
        """
        Function that allows users to view their cart including items and the price.
        """

        sub_total = 0

        # If the item is in the cart but the quantity is 0 remove it
        for item in self.cart:
            if item.quantity < 1:
                del item

        if self.cart is not []:
            for item in self.cart:
                print(f"{item.name}\n Options: {item.options}\n Price: {item.price}\n \
        Quantity: {item.quantity}")
                sub_total += item.price * item.quantity

            print(f"Subtotal: ${sub_total}\n Delivery Fee: ${sub_total * 0.1}\n Tax: \
      ${sub_total * 0.13}\n Total: ${sub_total * 1.23}")

            self.order_details["total"] = sub_total * 1.23

    def change_item_quantity(self):
        """
        Function that allows users to change the quantity of an item in their cart.
        """

        item_name = input("Which item do you want to change?")
        quantity = input("Change Item Quantity:")

        for item in self.cart:
            if item_name.lower == item.name.lower:
                item.quantity = quantity
                print(f"{item.name} quantity changed to {quantity}")
                # If change is made no need to search all items
                break

    def checkout(self):
        """
        Function that allows users to change details regarding their order and checkout.
        """

        address = input("Change address (press enter to skip):")
        dropoff_location = input(
            "Change delivery instructions (press enter to skip):")
        payment_method = input("Change payment method (press enter to skip):")
        promotions = float(input("Add promotion (or enter zero):"))
        tips = float(input("Add tips (or enter zero):"))

        # If the user did not skip changing details declare changes
        if address != "":
            print(f"Address changed to {address}")
        if dropoff_location != "":
            print(f"Dropoff location changed to {dropoff_location}")
        if payment_method != "":
            print(f"Payment method changed to {payment_method}")

        print(
            f"Your order total is: ${self.order_details['total'] - promotions + tips}")
        print("Please confirm all details before proceeding.")

    def track_order_progress(self, order_id, estimated_time, progress):
        """
        Function to track the progress of an order, where an order_id is created for 
        reference. Currently, it simulates tracking by printing the order's status.
        """

        self.order_details["order_id"] = order_id
        if "date and time" not in self.order_details:
            self.order_details["date and time"] = datetime.now()
        print(f"Tracking progress of order {order_id} from \
    {self.order_details['restaurant']}")
        print(f"Estimated time until delivery: {estimated_time}")
        self.progress = progress
        print(f"Status of delivery: {progress}")

    def restaurant_reviews(self):
        """
        Function to review orders made by the user.
        """

        if self.progress == "Delivered" and self.reviewed is False:
            print("Thank you for ordering from us!")
            self.review = input("Please rate your experience:")
            self.reviewed = True
            print("Thank you for your review!")

    def order_history(self):
        """
        Function to display a user's order history.
        """

        order_id = input("Please select an order to view details:")

        for order in self.past_orders:
            if order_id == order.order_details["order_id"]:
                print(f"Order ID: {order.order_details['order_id']}\n \
        Restaurant: {order.order_details['restaurant']}\n \
        Date and Time: {order.order_details['date and time']}\n \
        Items Ordered: {order.cart}\n Total Cost: ${order.order_details['total']}\n")


"""
The main program creates instances of each of the classes in the rest of the program 
and tests that each of them, when given correct input, give the correct output, and 
that the objects work together to create a cohesive delivery app. The input info would 
be account details, restaurants, menu items for a restaurants, and information required 
to make an order and track it, these are all stored within a database.
"""
if __name__ == "__main__":
    # Initialize tables in the database and allow management
    database_initialization.main()
    database = DatabaseManager()

    # Creating, logging into and changing details about user account
    account = Account()
    account.account_creation()
    # Inserting user into database
    database.save_user_details(account.user_id, account.user_name, account.user_email,
                               account.user_password, account.user_address, account.user_phone, account.user_dropoff)
    database.save_payment(account.user_main_payment +
                          "4360", account.user_id, account.user_main_payment)
    account.login()
    account.account_management()
    # Updating user details in database
    database.update_user_details(account.user_id, account.user_name, account.user_email,
                                 account.user_password, account.user_address, account.user_phone, account.user_dropoff)
    database.update_payment_details(
        account.user_main_payment + "1467", account.user_main_payment)

    # Creating restaurant examples
    osmows = Restaurant("Osmow's", "Mediterranean", "4.8")
    popeyes = Restaurant("Popeyes", "American", "4.3")
    # Adding restaurants to database
    database.add_restaurant("LocA_Osmows", osmows.name,
                            osmows.cuisine, osmows.rating)
    database.add_restaurant("LocE_Popeyes", popeyes.name,
                            popeyes.cuisine, popeyes.rating)

    # Creating a list of restaurants and searching
    restaurants = RestaurantView([osmows, popeyes])
    restaurants.find_restaurant()

    # Creating menu items for Osmow's
    fries = MenuItem("STIX", 3.38, {"Size": "Medium", "Extra Sauce": None})
    brownie = MenuItem("Brownie", 3.99, None)
    # Adding items to restaurant's menu
    database.add_menu_items("Fries_Osmows", "STIX", 3.38, {
                            "Size": "Medium", "Extra Sauce": "None"})
    database.add_menu_items("ChocBrownie_Osmows", "Brownie", 3.99, "None")

    # Creating an order from Osmow's and playing with the functionality of the cart,
    # tracking the order,and giving a review at the end
    order = Order("Osmow's", [fries, brownie], None)
    order.add_menu_item()
    order.add_menu_item()
    order.view_cart()
    order.change_item_quantity()
    order.checkout()
    # Creating order within database
    database.save_order("#1Osmows", account.user_id, "LocA_Osmows", order.order_details["total"], order.progress, order.order_details["date and time"], "#1Osmows", [
                        "Fries_Osmows", "ChocBrownie_Osmows"], order.cart)
    order.track_order_progress("#1Osmows", "1 hour", "Order Confirmed")
    # Updating delivery status
    database.update_order("#1Osmows", "Order Confirmed")
    order.track_order_progress("#1Osmows", "10 mins", "Out for Delivery")
    # Updating delivery status
    database.update_order("#1Osmows", "Out for Delivery")
    order.track_order_progress("#1Osmows", "0 mins", "Delivered")
    # Updating delivery status
    database.update_order("#1Osmows", "Delivered")
    order.restaurant_reviews()
    database.save_review("#1Osmows", "#1Osmows", account.user_id,
                         order.review, order.review, datetime.now())
    order.order_history()
