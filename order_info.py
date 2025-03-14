from fasthtml.common import *
from fastapi import FastAPI, Request, Form, status
import component
from controller import get_account, get_order_instance, get_course



def order_info_page(order, course):
    account = get_account()
    order_history = account.order_history
    # Render the account details
    return Div(
        component.navbar_component(),
        Header(
            "View Details",
            style="font-weight: 600; text-align:center; font-size: 30px;",
        ),
        Body(
            "You can view details or manage your account here.",
            style="text-align:center;",
        ),
        Hr(),
        # Main Container (Sidebar + Content)
        Div(
            # Sidebar (Left Side)
            Div(
                Button(
                    "Account Details",
                    style="text-align:left; color:black; background: transparent; border: none; cursor: pointer; height:45px; width:100%; outline: none;",
                    onclick="window.location.href='/account-details'",
                ),
                Hr(style="width:100%;text-align:left;margin-left:0;"),
                Button(
                    "View Orders",
                    style="text-align:left; color:black; background: transparent; border: none; cursor: pointer; height:45px; width:100%; outline: none;",
                    onclick="window.location.href='/orders'",
                ),
                Hr(style="width:100%;text-align:left;margin-left:0;"),
                Button(
                    "Logout",
                    style="text-align:left; color:red; background: transparent; border: none; cursor: pointer; height:45px; width:100%; outline: none;",
                ),
                Hr(style="width:100%;text-align:left;margin-left:0;"),
                style="width: 25%; min-width: 200px; padding: 20px; border-right: 1px solid #ccc;",
            ),
            # Account Details (Right Side) - Aligned to the Left
            Div(
                component.display_order_info_component(order, course),
                style="width: 75%; padding: 20px; text-align:left;",
            ),
            # Apply Flexbox
            style="display: flex; width: 100%;",
        ),
        style="width:100%; min-height: 100vh; background-color:white; color:black;",
    )
    
def setup_routes(rt):
    @rt("/orders&order_id={order_id}&course_id={course_id}")
    def get_order(request: Request, order_id: str, course_id: str):
        order = get_order_instance(order_id)
        course = get_course(course_id)
        return order_info_page(order, course)