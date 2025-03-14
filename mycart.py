from urllib import request
from fasthtml.common import *
from controller import *
from component import navbar_component

# global order1
# order1 = Order("1", 1000, app.search_course("2"), "1-1-2025")

def render_product_table(account):
    account = get_account()
    total_price = sum(course.price for course in account.cart.course) if len(account.cart.course) > 0 else 0
    return Table(
        Thead(Tr(Th("ID"), Th("Course Name"), Th("Price"), Th("Action"))),
        Tbody(
            *[
                Tr(
                    Td(course.id),
                    Td(course.title),
                    Td(f"${course.price:,}"),
                    Td(
                        Button("Delete", style="background-color: #F95959; color: white;border: none; border-radius: 5px; cursor: pointer;",
                               hx_confirm="Are you sure?",
                               hx_post=f"/delete/{course.id}",
                               hx_target="#product-table",
                               hx_swap="outerHTML"
                        )
                    )
                ) for course in account.cart.course
            ],
            # Total Price Row
            Tr(Td("", colspan="2"), Td(f"Total: ${total_price:,}", colspan="2", class_="total-row"))
        ),
        id="product-table",
        style="position: relative; top: 40px"
    )
def setup_routes(rt):
    @rt("/mycart")
    def get_products():
        # Search for the account
        account = get_account()  # Replace "1" with the account ID
        if account == None:
            return RedirectResponse("/login")

        return Div(navbar_component(),Html(
            Head(
                Title("My Cart"),
                Script(src="https://unpkg.com/htmx.org@1.9.5"),
                Style("""
                    body { background-color: white; color: black; font-family: Arial, sans-serif; padding-left: 100px; padding-right: 100px; }
                    table { width: 100%; border-collapse: collapse; border-radius: 10px;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);}
                    thead { border-bottom: 0.5px solid grey; }
                    th, td { padding: 12px; text-align: left; border: none;}
                    td:last-child, th:last-child { text-align: right; }

                    /* Minimal Delete Button */
                    .btn-delete {
                        padding: 6px 12px;
                        background-color: #00FFFF;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        font-size: 14px;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }
                    button:hover {
                        background-color: #2c3e50;
                    }
                    
                    .btn-delete:hover {
                        background-color: #00FFFF;
                    }

                    /* Total row style */
                    .total-row {
                        font-weight: bold;
                        background-color: #ffdddd;
                    }
                    .total-row td {
                        border-top: 2px solid red;
                    }
                """)
            ),
            Body(
                Div( 
                    H1("My Cart", style="text-align: center;"),
                    Img(src="https://static.vecteezy.com/system/resources/previews/019/787/018/original/shopping-cart-icon-shopping-basket-on-transparent-background-free-png.png", style="width:50px; height:25px;"),
                    style="display: flex; justify-content: center; align-items: center;  text-align: center;"
                ),
                Hr(),
                render_product_table(account),
                
                Div(
                    Button("Proceed to Checkout", 
                        # method="post",
                        # action="/add_order",
                        onclick="window.location.href='/billing'",
                        # hx_confirm="Are you sure?",
                        # hx_post="/add_order", 
                        # # hx_get="/billing",  # โหลดหน้า billing
                        # hx_target="body",  # แทนที่ทั้งหน้า
                        # hx_swap="outerHTML",  # แทนที่เนื้อหาเดิม
                        style="float: right; margin-top: 100px; padding-right: 40px; background-color: #F95959; color: white;border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer; "
                    ),
                ),
                
                Div(
                    Button("Back to Home",
                           onclick="window.location.href='/'",   
                            style="float: right; margin-top: 100px; padding-left: 40px; background-color: #F95959; color: white;border: none; border-radius: 5px; padding: 10px 20px; float:left; "
                    )
                )
            )
        ), style="margin: 0;"       
    )
   
    @rt("/delete/{course_id}")
    def delete_product(course_id: str):
        # Search for the account
        account = get_account()  # Replace "1" with the account ID
        if not account:
            return JSONResponse(content={"error": "Account not found"}, status_code=404)

        # Remove the course from the account's cart
        for course in account.cart.course:
            if course.id == course_id:
                account.cart.course.remove(course)
                break

        # Re-render the product table
        return render_product_table(account)


