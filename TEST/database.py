class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
    
    def __str__(self):
        return f"Product ID: {self.__id}, Name: {self.__name}, Price: {self.__price}"

    

class Book(Product):
    def __init__(self):
        pass
    
class Account:
    def __init__(self, id, email, password, name, username):
        self.__email = email
        self.__id = id
        self.__password = password
        self.__name = name
        self.__username = username
        self.__tel = None  # Phone number is not set initially
        self.__location = Location()
        self.__cart = []
        self.__course = []
        self.__order_history = []

    def edit_data(self, email, name, tel, location):
        self.__email = email
        self.__name = name
        self.__tel = tel
        self.__location.edit_location(location)
        
    def add_order_history(self, order):
        self.__order_history.append(order)
        
    def add_cart(self, product):   
        self.__cart.append(product)

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
    def __init__(self):
        self.__country = None
        self.__street_address = None
        self.__apt = None
        self.__suburb = None
        self.__city = None
        self.__province = None
        self.__postal_code = None

    def edit_location(self, location):
        self.__country = location[0]
        self.__street_address = location[1]
        self.__apt = location[2]
        self.__suburb = location[3]
        self.__city = location[4]
        self.__province = location[5]
        self.__postal_code = location[6]

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
    def __init__(self, title, id, price):
        self.__video = []
        self.__title = title
        self.__price = price
        self.__id = id
        self.__exam = []
        
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

class Payment:
    def __init__(self, payment_id, type, timestamp):
        self.__payment_id = payment_id
        self.__type = type
        self.__timestamp = timestamp
        
class Mycart:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__list_product = []
    
    
    @property    
    def mycart(self):
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
    
    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"Product ID: {self.__id}, Name: {self.__name}, Price: {self.__price}"
    
class Order:
    def __init__(self, id, total_money, course:Course):
        self.__id = id
        self.__total_money = total_money
        self.__course = course
        self.__datetime = None
        self.__payment_detail = None
        self.__order_status = "Pending"
        self.__list_order = []
        
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
    
    @order_status.setter
    def order_status(self, value):
        self.__order_status = value
    
    @property
    def order(self):
        return self.__list_order
    
    def add_order(self, x):
        self.__list_order.append(x)
        
        
class Platform:
    def __init__(self):
        self.__course = []
        self.__accounts = []  # List to store accounts
        
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
        self.__accounts.append(account)

    def search_account(self, id):
        for account in self.__accounts:
            if account.id == id:
                return account
        return None
        

app = Platform()

def set_initial_data():
    course1 = Course("Python", "1", 1000)
    vids1 = Video("Python Programing", "1", "vids/video1.mp4")
    vids2 = Video("Object Orient Programming", "2", "vids/video2.mp4")
    exam1 = Exam("Python Programming Quiz", "1")
    exam1.add_item(Item(1, "What is the output of 2 + 2?", "4", ["2", "3", "4", "5"]))
    exam1.add_item(Item(2, "What is the output of 2 * 2?", "4", ["2", "3", "4", "5"]))
    exam1.add_item(Item(3, "What is the output of 2 / 2?", "1", ["0", "1", "2", "3"]))
    exam1.add_item(Item(4, "What is the output of 2 - 2?", "0", ["0", "1", "2", "3"]))
    exam1.add_item(Item(5, "What is the output of 2 ** 2?", "4", ["2", "3", "4", "5"]))
    vids1 = Video("Python Programming", "1", "Test_path.mp4")
    
    course1.add_video(vids2)
    course1.add_video(vids1)
    course1.add_exam(exam1)
    
    app.add_course(course1)
    
set_initial_data()


# เดี๋ยวกูเอาไปใส่คู่กับ controller อันนี้ลอง
def pao_test():
    sample_account = Account(
        "1", "example@example.com", "password123", "John Doe", "johndoe"
    )
    
    sample_account.edit_data(
        "example@example.com",
        "John Doe",
        "1234567890",
        ["USA", "123 Main St", "Apt 4B", "Suburb", "New York", "NY", "10001"],
    )
    app.add_account(sample_account)
    
    order1 = Order("1", 1000, app.search_course("1"), "1-1-2025")
    order2 = Order("2", 1000, app.search_course("1"), "3-2-2025")
    
    sample_account.add_order_history(order1)
    sample_account.add_order_history(order2)
    

# Create instances of Mycart

cart1 = Mycart(1, "Shopping Cart 1", 0.0)
cart2 = Mycart(2, "Shopping Cart 2", 0.0)

# Create instances of Product
product1 = Product("101", "Laptop", 1200.00)
product2 = Product("102", "Mouse", 25.00)
product3 = Product("103", "Keyboard", 45.00)
product4 = Product("201", "Smartphone", 800.00)
product5 = Product("202", "Headphones", 150.00)

# Add products to cart1
cart1.add_product(product1)
cart1.add_product(product2)
cart1.add_product(product3)
cart1.add_product(product1)
cart1.add_product(product2)
cart1.add_product(product3)

# Add products to cart2
cart2.add_product(product4)
cart2.add_product(product5)

# for product in cart1.mycart:
#     print(product)



pao_test()
account = app.search_account("1")
order_history = account.order_history

