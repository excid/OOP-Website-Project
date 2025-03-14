class Product():
    def __init__(self):
        pass

class Book(Product):
    def __init__(self):
        pass
    
class Account:
    def __init__(self, email, password, name, username):
        self.__email = email
        self.__id = None
        self.__password = password
        self.__name = name
        self.__username = username
        self.__tel = None  # Phone number is not set initially
        self.__location = Location()
        self.__cart = Mycart()
        self.__course = []
        self.__order_history = []
        
    def change_password(self, new_password):
        self.__password = new_password

    def edit_data(self, email, name, tel, location):
        self.__email = email
        self.__name = name
        self.__tel = tel
        self.__location.edit_location(location)
        
    def search_order_in_order_history(self, id):
        for order in self.__order_history:
            if str(order.id) == str(id):
                return order
        return None
        
    def add_order_history(self, order):
        self.__order_history.append(order)
        
    def add_course(self, course):
        self.__course.append(course)
        
    def search_course(self, course_id):
        for course in self.__course:
            if course.id == course_id:
                return course
        return None
    
    def add_cart(self, product):   
        self.__cart = product
        
    @property
    def password(self):
        return self.__password
    
    @property
    def username(self):
        return self.__username
    
    @password.setter
    def password(self, value):
        self.__password = value
        
    @username.setter
    def username(self, value):
        self.__username = value
        
    @property
    def cart(self):
        return self.__cart
        
    @property
    def course(self):
        return self.__course

    @property
    def email(self):
        return self.__email
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @property
    def location(self):
        return self.__location
    
    @property
    def order_history(self):
        return self.__order_history
    
    @id.setter
    def id(self, value):
        self.__id = value

class Item:
    def __init__(self, number, question, answer, choices):
        self.__done = False
        self.__number = number
        self.__question = question
        self.__answer = answer
        self.__choices = choices
        self.__correctness = False
        
    @property
    def answer(self):
        return self.__answer
        
    @property
    def doness(self):
        return self.__done
        
    @property
    def question(self):
        return self.__question
    
    @property
    def choices(self):
        return self.__choices
    
    @property
    def correctness(self):
        return self.__correctness
        
    @property
    def number(self):
        return self.__number
        
    def select_choice(self, choice):
        self.__done = True
        if choice == self.__answer:
            self.__correctness = True
        else:
            self.__correctness = False
    
class Exam:
    def __init__(self, title, id):
        self.__id = id
        self.__doness = 0
        self.__score = 0
        self.__title = title
        self.__items = []
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def items(self):
        return self.__items
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value
        
    def add_item(self, item : Item):
        self.__items.append(item)
        
    def take_exam(self, number):
        for item in self.__items:
            if item.number == number:
                return item
    
    def grade(self):
        for item in self.__items:
            if item.correctness:
                self.__score += 1
        print(f"Your score is {self.__score}")
        
    def add_item(self, item : Item):
        self.__items.append(item)
    
    def doness(self):
        self.__doness = 0
        for item in self.__items:
            if item.doness:
                self.__doness += 1
        return self.__doness / len(self.__items)
    

class Location:
    def __init__(self, country=None, street_address=None, apt=None, suburb=None, city=None, province=None, postal_code=None):
        self.__country = country
        self.__street_address = street_address
        self.__apt = apt
        self.__suburb = suburb
        self.__city = city
        self.__province = province
        self.__postal_code = postal_code

    def edit_location(self, location):
        self.__country = location[0]
        self.__street_address = location[1]
        self.__apt = location[2]
        self.__suburb = location[3]
        self.__city = location[4]
        self.__province = location[5]
        self.__postal_code = location[6]
        
    def get_country(self):
        return self.__country

    @property
    def country(self):
        return self.__country

    @property
    def street_address(self):
        return self.__street_address

    @property
    def apt(self):
        return self.__apt

    @property
    def suburb(self):
        return self.__suburb

    @property
    def city(self):
        return self.__city

    @property
    def province(self):
        return self.__province

    @property
    def postal_code(self):
        return self.__postal_code

    
class Video:
    def __init__(self, title, id, path):
        self.__title = title
        self.__id = id
        self.__path = path
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def path(self):
        return self.__path
    
class Course:
    def __init__(self, title, id, price, img_url = None):
        self.__video = []
        self.__title = title
        self.__price = price
        self.__id = id
        self.__exam = []
        self.__img_url = img_url
        self.__progress = 10
        self.__detail = None
        
    @property
    def detail(self):
        return self.__detail
        
    @property
    def progress(self):
        return self.__progress
        
    @property
    def img(self):
        return self.__img_url
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def video(self):
        return self.__video
    
    @property
    def exam(self):
        return self.__exam
    
    @property
    def price(self):
        return self.__price
    
    @detail.setter
    def detail(self, value):
        self.__detail = value
    
    def add_video(self, value : Video):
        self.__video.append(value)
        
    def search_exam(self, exam_id):
        for exam in self.__exam:
            if exam_id == exam.id:
                return exam
        return None
        
    def search_video(self, title):
        for video in self.__video:
            if video.title == title:
                return video
        return None
    
    def add_exam(self, exam : Exam):
        self.__exam.append(exam)
        
class Mycart:
    def __init__(self):
        self.__id = 0
        self.__price = 0
        self.__list_product = []
    
    @property    
    def course(self):
        return self.__list_product
    
    def add_product(self, product):
        self.__list_product.append(product)
        
    def remove_product(self, product):
        self.__list_product.remove(product)
        
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def price(self):
        return self.__price
    
    def __str__(self):
        return f"Product ID: {self.__id}, Name: Null, Price: {self.__price}"

class Payment:
    def __init__(self, payment_id, payment_detail, amount, time):
        self.__type = "Debit / Credit Card"
        self.__payment_id = payment_id
        self.__payment_detail = payment_detail
        self.__amount = amount
        self.__time = time
        self.__card_number = None
        self.__expiry_date = None
        self.__cvv = None
        
    @property
    def type(self):
        return self.__type
        
    @property
    def card_number(self):
        return self.__card_number
    
    @card_number.setter
    def card_number(self, value):
        self.__card_number = value
        
    @property
    def expiry_date(self):
        return self.__expiry_date
    
    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value
        
    @property
    def cvv(self):
        return self.__cvv 
    
    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @property
    def payment_detail(self):
        return self.__payment_detail
    @property
    def payment_id(self):
        return self.__payment_id
    @property
    def amount(self):
        return self.__amount
    @property
    def time(self):
        return self.__time
    
    @payment_detail.setter
    def payment_detail(self, detail):
        self.__payment_detail = detail
    
    
class Order:
    def __init__(self, id, total_money, datetime):
        self.__id = id
        self.__total_money = total_money
        self.__course = []
        self.__datetime = datetime
        self.__payment_detail = None
        self.__location = None
        self.__order_status = "Pending"
        
    @property
    def location(self):
        return self.__location
        
    @property
    def course(self):
        return self.__course
    
    @property
    def id(self):
        return self.__id
    
    @property
    def total_money(self):
        return self.__total_money
    
    @property
    def payment_detail(self):
        return self.__payment_detail
    
    @property
    def datetime(self):
        return self.__datetime
    
    @property
    def order_status(self):
        return self.__order_status
    
    @payment_detail.setter
    def payment_detail(self, value):
        self.__payment_detail = value
        
    @order_status.setter
    def order_status(self, value):
        self.__order_status = value
        
    @property
    def order(self):
        return self.__list_order
    
    def add_location(self, location):
        self.__location = location

    def add_course(self, course):
        self.__course.append(course)
        
    
        

class Platform:
    def __init__(self):
        self.__course = []
        self.__accounts = []  # List to store accounts
        self.__generate_account_id = 0
        
    @property
    def accounts(self):
        return self.__accounts
    
    @property
    def course(self):
        return self.__course
    
    def search_course(self, id):
        for course in self.__course:
            if course.id == id:
                return course
        return None
        
    def add_course(self, value : Course):
        
        self.__course.append(value)
        
    def add_account(self, account):
        self.__generate_account_id += 1
        account.id = self.__generate_account_id
        self.__accounts.append(account)

    def search_account(self, id):
        for account in self.__accounts:
            if account.id == id:
                return account
        return None
        
app = Platform()

def generate_mock_data():

    # 📚 Create Courses
    course1 = Course("Python for Beginners", "1", 1000, "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg")
    course2 = Course("Advanced Python", "2", 1500, "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg")
    course3 = Course("Django Web Development", "3", 2000, "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg")
    course4 = Course("C for Beninging", "4", 1500, "https://www.khmer168.com/wp-content/uploads/2024/01/c-tutorial-for-beginners.png")

    # 🎥 Add Videos to Courses
    course1.add_video(Video("Intro to Python", "1", "/vids/1.polynomial.mp4"))
    course1.add_video(Video("Variables & Data Types", "2", "/vids/2.polynomial.mp4"))
    course1.add_video(Video("Control Flow", "3", "/vids/3.polynomial.mp4"))

    course2.add_video(Video("Advanced OOP Concepts", "3", "vids/advanced_oop.mp4"))
    course2.add_video(Video("Generators & Iterators", "4", "vids/generators.mp4"))

    course3.add_video(Video("Django Models", "5", "vids/django_models.mp4"))
    course3.add_video(Video("Django Views & Templates", "6", "vids/django_views.mp4"))
    
    course4.add_video(Video("Intro to C", "7", "vids/c_intro.mp4"))

    # 📝 Create Exams
    exam1 = Exam("Python Basics Quiz", "1")
    exam1.add_item(Item(1, "What is 2 + 2?", "4", ["2", "3", "4", "5"]))
    exam1.add_item(Item(2, "What is the keyword for defining a function?", "def", ["def", "fun", "define", "func"]))

    exam2 = Exam("Advanced Python Quiz", "2")
    exam2.add_item(Item(1, "What does `yield` do?", "Returns a generator", ["Returns a generator", "Ends function", "Throws error", "None"]))

    exam3 = Exam("Django Essentials Quiz", "3")
    exam3.add_item(Item(1, "What command creates a Django project?", "django-admin startproject", 
                        ["django-admin startproject", "django createproject", "django start", "django-admin new"]))
    
    exam4 = Exam("C Basics Quiz", "4")
    exam4.add_item(Item(1, "What is Pointer", "4", ["A finger", "RAM Address", "My name", "I don't know"]))
    exam4.add_item(Item(2, "What is the output of 2 * 2?", "4", ["2", "3", "4", "5"]))

    # 📌 Attach Exams to Courses
    course1.add_exam(exam1)
    course2.add_exam(exam2)
    course3.add_exam(exam3)
    course4.add_exam(exam4)

    # 🎓 Add Courses to Platform
    app.add_course(course1)
    app.add_course(course2)
    app.add_course(course3)
    app.add_course(course4)

    # 👤 Create User Accounts
    user1 = Account("alice@example.com", "securepass", "Alice Johnson", "alicej")
    user2 = Account("bob@example.com", "mypassword", "Bob Smith", "bobsmith")
    admin = Account("admin", "admin", "admin", "admin")

    # 🌎 Assign Locations
    location1 = Location("USA", "456 Oak St", "Apt 12", "Downtown", "San Francisco", "CA", "94110")
    location2 = Location("Canada", "789 Maple Ave", None, "Suburb", "Toronto", "ON", "M4B 1B3")

    user1.edit_data("alice@example.com", "Alice Johnson", "1234567890", 
                    ["USA", "456 Oak St", "Apt 12", "Downtown", "San Francisco", "CA", "94110"])
    
    user2.edit_data("bob@example.com", "Bob Smith", "9876543210", 
                    ["Canada", "789 Maple Ave", None, "Suburb", "Toronto", "ON", "M4B 1B3"])

    # Add products to carts
    user1.cart.add_product(course1)
    user1.cart.add_product(course3)

    user2.cart.add_product(course2)

    # Link cart to users
    for course in app.course:
        admin.add_course(course)

    # 🛍 Create Orders
    order1 = Order("101", 1000, "2024-03-10 12:00:00")
    order1.add_course(course1)
    order2 = Order("102", 1500, "2024-03-11 14:30:00")
    order2.add_course(course2)

    # 💳 Add Payment Details
    order1.payment_detail = Payment("201", "Credit Card", 1000, "2024-03-10 12:00:00")
    order2.payment_detail = Payment("202", "PayPal", 1500, "2024-03-11 14:30:00")

    # ✅ Add Order History
    user1.add_order_history(order1)
    user2.add_order_history(order2)

    # 🎓 Enroll Users in Courses
    user1.add_course(course1)
    user2.add_course(course2)
    user1.add_course(course3)

    # 🔥 Add Users to Platform
    app.add_account(user1)
    app.add_account(user2)
    app.add_account(admin)
  # ✅ Return the platform with all mock data

generate_mock_data()
# 🎉 Generate the Mock Data
# ✅ Example: Fetch User Data



# def set_initial_data():
#     course1 = Course("Python", "1", 1000)
#     vids1 = Video("Python Programing", "1", "vids/video1.mp4")
#     vids2 = Video("Object Orient Programming", "2", "vids/video2.mp4")
#     exam1 = Exam("Python Programming Quiz", "1")
#     exam1.add_item(Item(1, "What is the output of 2 + 3?", "4", ["2", "3", "4", "5"]))
#     exam1.add_item(Item(2, "What is the output of 2 * 2?", "4", ["2", "3", "4", "5"]))
#     exam1.add_item(Item(3, "What is the output of 2 / 2?", "1", ["0", "1", "2", "3"]))
#     exam1.add_item(Item(4, "What is the output of 2 - 2?", "0", ["0", "1", "2", "3"]))
#     exam1.add_item(Item(5, "What is the output of 2 ** 2?", "4", ["2", "3", "4", "5"]))
#     course1.add_video(vids2)
#     course1.add_video(vids1)
#     course1.add_exam(exam1)
    
    
#     app.add_course(course1)
      
# set_initial_data()

# # เดี๋ยวกูเอาไปใส่คู่กับ controller อันนี้ลอง
# def pao_test():
#     sample_account = Account(
#         "1", "example@example.com", "password123", "John Doe", "johndoe"
#     )
#     sample_account.edit_data(
#         "example@example.com",
#         "John Doe",
#         "1234567890",
#         ["USA", "123 Main St", "Apt 4B", "Suburb", "New York", "NY", "10001"],
#     )
#     app.add_account(sample_account)
#     order1 = Order("2", 1000, app.search_course("1"))
    
#     location1 = Location("USA", "123 Main St", "Apt 4B", "Suburb", "New York", "NY", "10001")
#     order1.payment_detail = Payment("1", "Credit Card", "2021-10-10 10:00:00", location1)
#     sample_account.add_order_history(order1)
#     sample_account.add_course(app.search_course("1"))
    
# pao_test()
# account = app.search_account("1")
# order_history = account.order_history


