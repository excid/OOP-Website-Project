from fasthtml.common import *
from database import *

order_list = []
def render_product_table():
    total_price = sum(p.price for p in cart1.mycart)
    return Table(
        Thead(Tr(Th("ID"), Th("Product Name"), Th("Price"), Th("Action"))),
        Tbody(
            *[
                Tr(
                    Td(p.id),
                    Td(p.name),
                    Td(f"${p.price:,}"),
                    Td(
                        Button("Delete", style="background-color: #F95959; color: white;border: none; border-radius: 5px;",
                               hx_confirm="Are you sure?",
                               hx_post=f"/delete/{p.id}",
                               hx_target="#product-table",
                               hx_swap="outerHTML"
                        )
                    )
                ) for p in cart1.mycart
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
        return Html(
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
                render_product_table(),
                
                Div(
                    Button("Proceed to Checkout", 
                        hx_confirm="Are you sure?",
                        hx_post="/add_order", 
                        hx_swap="outerHTML",
                        hx_target="#product-table",
                        hx_redirect="/billing",
                        
                        
                         
                        style="float: right; margin-top: 100px; padding-right: 40px; background-color: #F95959; color: white;border: none; border-radius: 5px; padding: 10px 20px; cursor: pointer; "
                    ),
                ),
                
                Div(
                    Button("Back to Home", 
                        hx_get="/",  
                        hx_target="body",    
                        style="float: right; margin-top: 100px; padding-left: 40px; background-color: #F95959; color: white;border: none; border-radius: 5px; padding: 10px 20px; float:left;"
                    ),
                )
            )
        )       
   
    @rt("/delete/{product_id}")
    def delete_product(product_id: str):
        global cart1
        for p in cart1.mycart:
            print(cart1.mycart)
            print(p.id)
            if p.id == product_id:
                cart1.mycart.remove(p.id, p.name, p.price)
                break
        return render_product_table()
    
    @rt("/add_order")
    def post_order():
        for p in cart1.mycart:
            order1 = Order(p.id, p.name, p.price)
            order_list.append(order1)
            
        cart1.mycart.clear() 
        x = len(cart1.mycart)
        print(x)
        return "Order has been added to the order list."
    
