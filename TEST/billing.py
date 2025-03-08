from fasthtml.common import *
from database import *
from mycart import *
from mycart import order_list

print(order_list)

def setup_routes(rt):
    @rt("/billing")
    def setup_routes():  
        return Container(
            H1("Billing Information"),
            Form(
                # Text input
                Label("Username:", 
                    Input(type="text", id="username", name="username", value=account.name, required=True)),
                
                # Number input for phone
                Label("Tel:", 
                    Input(type="number", id="tel", name="tel", value=account.tel, required=True)),
                
                # Email input
                Label("Email:", 
                    Input(type="email", id="email", name="email", value=account.email, required=True)),
                
                # Address inputs
                Label("Country:", 
                    Input(type="text", id="Country", name="Country", value=account.location.country, required=True)),
                
                Label("City:", 
                    Input(type="text", id="City", name="City", value=account.location.city, required=True)),
                
                Label("Suburb:",
                    Input(type="text", id="suburb", name="suburb", value=account.location.suburb, required=True)), 
                
                # Checkbox
                Label(
                    CheckboxX(id="agree", name="agree", label="I agree to terms", required=True)
                ),
                
                # Submit Button
                Button("Submit", type="submit"),
                method="post",
                action="/submit",
                hx_post="/submit",  # ใช้ HTMX เพื่อให้ส่งข้อมูลแบบ AJAX
                hx_swap="outerHTML",  # เปลี่ยนหน้าหลังส่งข้อมูล
                hx_redirect="/submit"  # ให้เปลี่ยนหน้าไปที่ /submit
            )
        )
    @rt("/submit")
    def post_submit():
        return Title("Order Submitted"), Container(
            H1("Order Submitted", style="color: #00FFFF;"),
            P(f"Order {account.order1['order_id']} has been submitted."),
            P("Thank you for your order.")
        )