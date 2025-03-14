from database import *
from fasthtml.common import *
from datetime import datetime

account = None
course = None

def accessed_account(account_id):
    global account
    account = app.search_account(account_id)

def get_account():
    global account
    return account

def accessed_course(course_id):
    global course
    course = account.search_course(course_id)

def get_account_course():
    return account.course

def get_course(course_id):
    course = app.search_course(course_id)
    return course

def get_all_course():
    return app.course

def get_all_video():
    return course.video

def get_exam(exam_id):
    exam = course.search_exam(exam_id)
    return exam
    
def get_all_quiz():
    return course.exam

def grading(form_data, exam):
    for item in exam.items:
            try:
                choice = form_data[f"q{item.number}"]  # Access user's choice for each question
                if choice == item.answer:
                    exam.score += 1
            except:
                pass
            
def change_password(new_password, confirm_password):
    if new_password != confirm_password:
        return "Passwords do not match"
    account.change_password(new_password)
    
def edit_account_data(email,name,tel, adress):
    account.edit_data(email,name,tel, adress)
    
def get_order_instance(order_id):
    order = account.search_order_in_order_history(order_id)
    return order

def billing(username:str, email:str, country:str, city:str, suburb:str, province:str, postal_code:int):
    global transaction, location
    price = sum(p.price for p in account.cart.course)
    location = Location(country, None, None, suburb, city, province, postal_code)
    transaction = Payment("1", f"username : {username}, email : {email}, country: {country}, city : {city}, suburb : {suburb}, province : {province}, postal_code : {postal_code}",price,datetime.now())
    
def payment(card_number:str, expiry_date:str, cvv:str):
    global transaction
    transaction.card_number = card_number
    transaction.expiry_date = expiry_date
    transaction.cvv = cvv
    
def get_transaction():
    global transaction
    return transaction

def add_to_cart(course_id):
    courses = app.search_course(course_id)
    print(course_id)
    if account != None: 
        if courses not in account.cart.course and courses not in account.course:
            account.cart.add_product(courses)
    else:
        return Response(status_code=200, headers={"HX-Location": "/login"})
        
def handle_signup(username, password, email, first_name, last_name):
    global account
    for accounts in app.accounts:
        if accounts.username == username:
            return Div("Username already exists", style="color: red; text-align: center;")
        elif accounts.email == email:
            return Div("Email already exists", style="color: red; text-align: center;")
    if account == None:
        name = f"{first_name} {last_name}"
        account = app.add_account(Account(email, password, name, username))
        return Response(status_code=200, headers={"HX-Location": "/login"})
    else:
        return Div("You are already signed in", style="color: red; text-align: center;")
    
def handle_signin(username, password):
    all_account = app.accounts
    for accounts in all_account:
        if (accounts.username == username or accounts.email == username) and accounts.password == password:
            accessed_account(accounts.id)
            return Response(status_code=200, headers={"HX-Location": "/my-course"})
    return Div("Username or password is incorrect", style="color: red; text-align: center;")

def post_order():
    # Search for the account
    account = get_account()  # Replace "1" with the account ID
    if not account:
        return JSONResponse(content={"error": "Account not found"}, status_code=404)

    total_price = sum(p.price for p in account.cart.course)
    order = Order(
        id=str(len(account.order_history) + 1),  
        total_money=total_price,
        datetime=datetime.now()
    )
    
    order.payment_detail = transaction
    order.add_location(location)

    # Add cart items to the order
    for course in account.cart.course:
        order.add_course(course)

    # Add the order to the account's order history
    account.add_order_history(order)

    # Clear the account's cart after checkout
    add_course_from_cart_to_account()
    account.cart.course.clear()
    # Redirect to the billing page
    return order

def add_course_from_cart_to_account():
    for course in account.cart.course:
        account.add_course(course)
        
def logout():
    global account
    account = None
        