# from fasthtml.common import *
# from database import *  # Ensure account is properly imported
# from mycart import * # Ensure order1 is properly imported


# def setup_routes(rt):
#     @rt("/billing")
#     def billing_page():  # Renamed to avoid function name conflict
#         return Container(
#             Head(
#                 Title("Billing Information", style="text-align: center;"),
#                 Style("""
#                     body { 
#                         background-color: white; 
#                         color: black; 
#                         font-family: Arial, sans-serif; 
#                         padding-left: 250px;  /* Increased from 150px to 250px */
#                         padding-right: 250px; /* Increased from 150px to 250px */
#                     }
#                 """)
#             ),
#             Body(
#                 Div( 
#                     H1("Billing", style="text-align: center; color: black;"),
#                     style="display: flex; justify-content: center; align-items: center; text-align: center;"
#                 ),
#                 Form(
#                     # Text input
#                     Label("Username:", 
#                         Input(type="text", id="username", name="username", value=account.name, required=True)
#                         ,style="color:black;"),
                    
#                     # Number input for phone
#                     Label("Tel:", 
#                         Input(type="number", id="tel", name="tel", value=account.tel, required=True)
#                         ,style="color:black;"),
                    
#                     # Email input
#                     Label("Email:", 
#                         Input(type="email", id="email", name="email", value=account.email, required=True)
#                         ,style="color:black;"),
                    
#                     # Address inputs
#                     Label("Country:", 
#                         Input(type="text", id="country", name="country", value=account.location.country, required=True)
#                         ,style="color:black;"),
                    
#                     Label("City:", 
#                         Input(type="text", id="city", name="city", value=account.location.city, required=True)
#                         ,style="color:black;"),
                    
#                     Label("Suburb:",
#                         Input(type="text", id="suburb", name="suburb", value=account.location.suburb, required=True)
#                         ,style="color:black;"), 
                    
#                     # Checkbox
#                     Label(
#                         CheckboxX(id="agree", name="agree", label="I agree to terms", required=True)
#                         ,style="color:black;",
#                     ),
                    
#                     # Submit Button
#                     Button("Submit", type="submit"),
#                     method="post",
#                     action="/submit",
#                     hx_post="/submit",  # Use HTMX for AJAX submission
#                     hx_swap="outerHTML",  # Swap the page content after submission
#                     hx_redirect="/submit"  # Redirect to /submit page
#                 ),
#             )
#         )
        

#     @rt("/submit")
#     def post_submit():
#         global order1
#         order1.order_status = "Submitted"
#         return Title("Order Submitted"), Div(
#             H3("Payment Complete Order Submitted", style="color: black; text-align: center; margin-top: 100px;"),
#             Hr(),
#             P(f"Order {order1.id} has been submitted.",style="color: black;text-align: center;"),  # Fixed incorrect dictionary access
#             P("Thank you for your order.",style="color: black;text-align: center;"),
#         ) i want before status change go transaction route if succes status should be change if not not change i use fasthtml frmaework




from fasthtml.common import *
from database import *  # Ensure account is properly imported
from mycart import *  # Ensure order1 is properly imported
from component import navbar_component
from datetime import datetime
from controller import *



def setup_routes(rt):
    @rt("/billing")
    def billing_page():
        account = get_account()
        return navbar_component(),Container(
            Head(
                Title("Billing Information", style="text-align: center;"),
                Style("""
                    html, body {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        background-color: white;
                        color: #333; 
                        font-family: 'Arial', sans-serif; 
                    }
                    .container {
                        max-width: 600px;
                        margin: 50px auto; /* ปรับ margin-top */
                        padding: 20px;
                        background: white;
                        border-radius: 10px;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        animation: fadeIn 0.5s ease-in-out;
                    }
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(-20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                    h1 {
                        color: black;
                        font-size: 2.5rem;
                        margin-bottom: 20px;
                    }
                    label {
                        display: block;
                        margin-bottom: 8px;
                        font-weight: bold;
                        color: #555;
                        
                    }
                    input[type="text"], input[type="number"], input[type="email"] {
                        width: 100%;
                        padding: 10px;
                        margin-bottom: 20px;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        font-size: 1rem;
                        transition: border-color 0.3s ease;
                    }
                    input[type="text"]:focus, input[type="number"]:focus, input[type="email"]:focus {
                        border-color: #3498db;
                        outline: none;
                    }
                    .checkbox-label {
                        display: flex;
                        align-items: center;
                        margin-bottom: 20px;
                    }
                    .checkbox-label input {
                        margin-right: 10px;
                    }
                    button {
                        width: 100%;
                        padding: 12px;
                        background-color: #F95959;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 1rem;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }
                    button:hover {
                        background-color: #F95959;
                    }
                    .order-summary {
                    margin-bottom: 20px;
                    padding: 15px;
                    background-color: #f9f9f9;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                    }
                    .order-summary h3 {
                        margin-bottom: 10px;
                        font-size: 1.5rem;
                        color: #2c3e50;
                    }
                    .order-summary p {
                        margin: 5px 0;
                        color: #555;
                    }
                    
                """)
            ),
            Body(
                Div( 
                    H1("Billing", style="text-align: center; color: black;"),
                    style="display: flex; justify-content: center; align-items: center; text-align: center;"
                ),
                Hr(),
                Form(
                    # Text input
                    Label("Username:", 
                        Input(type="text", id="username", name="username", value=account.name, required=True)
                        ,style="color:black;"),
                    
                    # Email input
                    Label("Email:", 
                        Input(type="email", id="email", name="email", value=account.email, required=True,)
                        ,style="color:black;"),
                    
                    # Address inputs
                    Label("Country:", 
                        Input(type="text", id="country", name="country", value=account.location.country, required=True)
                        ,style="color:black;"),
                    
                    Label("City:", 
                        Input(type="text", id="city", name="city", value=account.location.city, required=True)
                        ,style="color:black;"),
                    
                    Label("Suburb:",
                        Input(type="text", id="suburb", name="suburb", value=account.location.suburb, required=True)
                        ,style="color:black;"), 
                    
                    # Number input for province
                    Label("Province:", 
                        Input(type="text", id="province", name="province", value=account.location.province, required=True)
                        ,style="color:black;"),
                    
                    # postle code
                    Label("Postal Code:", 
                        Input(type="number", id="postal_code", name="postal_code", value=account.location.postal_code, required=True)
                        ,style="color:black;"),
                    
                    
                    # Div(
                    # H3("Order Summary", style="color: #2c3e50;"),
                    # P(f"Course: {account.cart.name}", style="color: #555;"),  # Display the course title
                    # P(f"Total Price: ${sum(course.price for course in account.cart.course):,}", style="color: #555;"),  # Display the total price
                    # class_="order-summary"
                    # ),                   
                    Div(
                        H3("Order Summary", style="color: #2c3e50;"),
                        Div(
                            Div(
                                Div(*[P(f"Course: {name.title}", style="color: #555; margin-right: 20px; padding-left: -50px") for name in account.cart.course]),  # Display the course title
                                P(f"Total Price: ${sum(course.price for course in account.cart.course):,}", style="color: #555; margin: 0;"),  # Display the total price
                                style="flex: 1; padding-right: 20px;"  # Add padding to separate text from image
                            ),
                            Img(src="\image\logo.png", style="width: 200px; height: 150px; border-radius: 10px;"),  # Placeholder image
                            style="display: flex; align-items: center; gap: 50px; margin: 20px; padding: 20px;"  # Flexbox layout with margin and padding
                        ),
                        class_="order-summary"
                    ),
                    
                    Label(
                        CheckboxX(id="agree", name="agree", label="I agree to terms", required=True)
                        ,style="color:#F95959;",
                    ),
                    
                    Button("Proceed to Payment", type="submit"),
                        method="post",
                        action="/transaction",  # Redirect to transaction page
                        #hx_post="/transaction",  # Use HTMX for AJAX submission
                        hx_swap="outerHTML",  # Swap the page content after submission
                        hx_redirect="/transaction"  # Redirect to /transaction page
                    ),
                    class_="container"
                ),
            )
        

    @rt("/transaction")
    def payment_page(username:str, email:str, country:str, city:str, suburb:str, province:str, postal_code:int):
        billing(username, email, country, city, suburb, province, postal_code)
        return Container(
            Head(
                Title("Payment Information", style="text-align: center;"),
                Style("""
                    html, body {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        background-color: white;
                        color: #333; 
                        font-family: 'Arial', sans-serif; 
                    }
                    .container {
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                        background: white;
                        height: 100vh; /* Full screen height */
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        animation: fadeIn 0.5s ease-in-out;
                    }
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(-20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                    h1 {
                        color: black;
                        font-size: 2.5rem;
                        margin-bottom: 20px;
                    }
                    label {
                        display: block;
                        margin-bottom: 8px;
                        font-weight: bold;
                        color: #555;
                    }
                    input[type="text"] {
                        width: 100%;
                        padding: 10px;
                        margin-bottom: 20px;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        font-size: 1rem;
                        transition: border-color 0.3s ease;
                    }
                    input[type="text"]:focus {
                        border-color: #3498db;
                        outline: none;
                    }
                    button {
                        width: 100%;
                        padding: 12px;
                        background-color: #3498db;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 1rem;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }
                    button:hover {
                        background-color: #2980b9;
                    }
                """)
            ),
            Body(
                Div(
                    H1("Payment Information", style="text-align: center;"),
                    Form(
                        # Card Number
                        Label("Card Number:",
                            Input(type="text", id="card_number", name="card_number", placeholder="1234 5678 9012 3456", required=True)
                        ),
                        # Expiry Date
                        Label("Expiry Date:",
                            Input(type="text", id="expiry_date", name="expiry_date", placeholder="MM/YY", required=True)
                        ),
                        # CVV
                        Label("CVV:",
                            Input(type="text", id="cvv", name="cvv", placeholder="123", required=True)
                        ),
                        # Submit Button
                        Button("Pay Now", type="submit"),
                        method="post",
                        action="/process_payment",  # Process transaction
                        # hx_post="/process_payment",  # Use HTMX for AJAX submission
                        hx_swap="outerHTML",  # Swap the page content after submission
                        hx_redirect="/process_payment"  # Redirect to /process_payment
                    ),
                    class_="container"
                ),
            )
        )

    @rt("/process_payment")
    async   def process_payment(request: Request, sess, card_number:str, expiry_date:str, cvv:str ):
            account = get_account()
            payment(card_number, expiry_date, cvv)
            # Simulate transaction processing
            # form_data = {
            # "username": request.form.get("username"),
            # }
            
            # บันทึกข้อมูลการชำระเงิน
            # transaction = handle_payment_form(form_data)
            
            payment_successful = simulate_payment() 
            order = post_order()
            sess["order_id"] = str(order.id)  # Store order ID as a string
            print("Session after storing order_id:", sess)  # Debugging
            
            print("Session after storing order_id:", request.session) 
            if payment_successful:
                order.order_status = "Submitted"
                return Redirect("/submit")  # Redirect to the submit page on success
            else:
                return Div(
                    H3("Payment Failed", style="color: black; text-align: center; margin-top: 100px;"),
                    P("Please check your transaction details and try again.", style="color: black; text-align: center;"),
                    A("Retry Payment", href="/billing", style="color: blue; text-align: center; display: block;")
                )

    @rt("/submit")
    def post_submit(request: Request, sess):
        print("2")
        order = request.session.get("order")
        print("Session before retrieving order_id:", sess)  # Debugging

        order_id = sess.get("order_id") 
        print(order_id)
        if not order_id:
            return Div(
                H3("No Order Found", style="color: black; text-align: center; margin-top: 100px;"),
                P("Please complete the transaction first.", style="color: black; text-align: center;"),
                A("Go to Payment", href="/transaction", style="color: blue; text-align: center; display: block;")
            )
        return Container(
            Head(
                Title("Order Submitted", style="text-align: center;"),
                Style("""
                    html, body {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        background-color: white;
                        color: #333; 
                        font-family: 'Arial', sans-serif; 
                    }
                    .container {
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                        background: white;
                        height: 100vh; /* Full screen height */
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        animation: fadeIn 0.5s ease-in-out;
                    }
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(-20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                    h3 {
                        color: #2c3e50;
                        font-size: 2rem;
                        margin-bottom: 20px;
                    }
                    p {
                        color: #555;
                        font-size: 1.1rem;
                        margin-bottom: 10px;
                    }
                """)
            ),
            Body(
                Div(
                    H3("Payment Complete - Order Submitted", style="text-align: center;"),
                    Hr(),
                    P(f"Order {order_id} has been submitted.", style="text-align: center;"),
                    P("Thank you for your order.", style="text-align: center;"),
                    A("View Transactions", href="/transactions", style="color: blue; text-align: center; display: block; margin-top: 20px;"),
                    class_="container"
                ),
            )
        )
        
    @rt("/transactions")
    def show_transactions():
        transaction = get_transaction()
        print(transaction)
        return Container(
            Head(
                Title("Transaction List", style="text-align: center;"),
                Style("""
                    html, body {
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        background-color: white;
                        color: #333; 
                        font-family: 'Arial', sans-serif; 
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        background: white;
                        height: 100vh; /* Full screen height */
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        animation: fadeIn 0.5s ease-in-out;
                    }
                    @keyframes fadeIn {
                        from { opacity: 0; transform: translateY(-20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                    h3 {
                        color: #2c3e50;
                        font-size: 2rem;
                        margin-bottom: 20px;
                    }
                    p {
                        color: #555;
                        font-size: 1.1rem;
                        margin-bottom: 10px;
                    }
                """)
            ),
            Body(
                Div(
                    H3("Transaction List", style="text-align: center;"),
                    *[
                        Div(
                            P(f"Payment ID: {transaction.payment_id}"),
                            P(f"Detail: {transaction.payment_detail}"),
                            P(f"Amount: ${transaction.amount}"),
                            P(f"Time: {transaction.time}"),
                            P(f"Card_number: {transaction.card_number}"),
                            P(f"Expiry_date: {transaction.expiry_date}"),
                            P(f"Cvv: ${transaction.cvv}"),
                            Hr(),
                        )
                    ],
                    class_="container"
                ),
                Div(
                        Button("Back"), onclick="window.location.href='/my-course'",
                        style="text-align: center;"
                    )


            )
        )

def simulate_payment():
    # Simulate a transaction process (e.g., 80% success rate)
    return True  # 80% chance of success


    