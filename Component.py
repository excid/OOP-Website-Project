from fasthtml.common import *
from controller import *
from itertools import chain

def navbar_component():
    return Div(
        # Navbar container with flex layout for left/right alignment
        Div(
            # Left side: Brand/logo
            Div(
                A(
                    Img(
                        src="/image/logo.png",  # Adjust the path as needed
                        style="width: 50x; height: 40px; margin-right: 10px;",
                    ),
                    H2("CAM'ERA", style="margin: 0; color: inherit;"),
                    style="display: flex; align-items: center; text-decoration: none; color: inherit;",
                    href="/",
                ),
            ),
            # Right side: Navigation links
            Div(
                A(
                    Img(
                        src="/image/cart.png",
                        style="width: 20px; height: 20px; margin-right: 10px;",
                    ),
                    "My Cart",
                    href="/mycart",
                    style="padding: 10px; text-decoration: none; color: inherit; margin-right: 50px",
                ),
                A(
                    Img(
                        src="/image/course.png",
                        style="width: 20px; height: 20px; margin-right: 10px;",
                    ),
                    "Course",
                    href="/course",
                    style="padding: 10px; text-decoration: none; color: inherit;  margin-right: 50px",
                ),
                closed_account_dropdown(),
                style="display: flex; align-items: center;",
            ),
            style=(
                "display: flex; justify-content: space-between; align-items: center; "
                "padding: 10px 20px; background-color: #fff; border-bottom: 1px;"
            ),
        ),
        style="width: 100%;-webkit-user-select: none; -ms-user-select: none; user-select: none;",
    )


def closed_account_dropdown():
    return (
        Div(
            Div(
                Img(
                    src="/image/arrow_down.png",  # Arrow icon
                    style="width: 10px; height: 5px; margin-right: 5px;",
                ),
                "My Account",
                style="padding: 10px; text-decoration: none; color: inherit; cursor: pointer;",
            ),
            style="position: relative; margin-right: 30px;",
            hx_get="/open-account-dropdown",
            hx_swap="outerHTML",
        ),
    )


def opened_account_dropdown():
    return (
        Div(
            A(
                Img(
                    src="/image/arrow_up.png",  # Arrow icon
                    style="width: 10px; height: 5px; margin-right: 5px;",
                ),
                "My Account",
                style="padding: 10px; text-decoration: none; color: inherit; cursor: pointer; ",
            ),
            Div(
                # Dropdown menu (Initially hidden)
                A(
                    "My Course",
                    href="/my-course",
                    style="display: block; padding: 5px; text-decoration: none; color: black;",
                ),
                Hr(style="margin-top:0px; margin-bottom: 0px;"),
                A(
                    "View Details",
                    href="/account-details",
                    style="display: block; padding: 5px; text-decoration: none; color: black;",
                ),
                style="position: absolute; border: 1px solid black; border-radius: 5px; width: 150px; margin-left:-10px; margin-top: 20px; background-color:white; z-index: 1000;",
            ),
            style="position: relative; margin-right: 30px;",
            hx_get="/close-account-dropdown",
            hx_swap="outerHTML",
        ),
    )


def password_no_popup_component():
    return Div(
        A(
            "Change Password",
            style="width: 130px; text-align: left;",
            hx_get="/change-password",
            hx_target="#password-popup",
        ),
        id="password-popup",
    )


def change_password_component():
    return Div(
        A(
            "Change Password",
            style="width: 130px; text-align: left;",
            hx_get="/back-from-change-password",
            hx_target="#password-popup",
        ),
        Form(
            # Common style for all form rows
            Div(
                Div(
                    P(
                        "New Password: ",
                        style="flex: 0 0 150px; text-align: left; margin-right: 20px; align-self: center; color:black;",
                    ),
                    Input(
                        value="",
                        id="new_password",
                        name="new_password",
                        type="password",
                        style="flex: 1; height: 30px; border: 1px solid #ddd; border-radius: 4px;",
                    ),
                    P(
                        "Confirm Password: ",
                        style="flex: 0 0 150px; text-align: left; margin-right: 20px; align-self: center; color:black;",
                    ),
                    Input(
                        value="",
                        id="confirm_password",
                        name="confirm_password",
                        type="password",
                        style="flex: 1; height: 30px; border: 1px solid #ddd; border-radius: 4px;",
                    ),
                    style="align-items: center; margin-bottom: 15px; gap: 10px;",
                ),
            ),
            Div(
                Button(
                    "Save Changes",
                    type="submit",
                    style="padding: 10px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;",
                ),
                style="margin-top: 30px; display: flex; justify-content: flex-end;",
            ),
            style="max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border-radius: 8px;",
            action="/change-password-submit",
            method="post",
        ),
    )


def display_account_details_component():
    account = get_account()
    return Div(
        Div(
            H2("Account Details", style="text-align:left;color:inherit;"),
            Img(
                src="./image/edit.png",
                style="width: 30px; height: 30px; cursor: pointer;margin-left:10px;",
                hx_get="/account-details-edit",
                hx_target="#main-content",
            ),
            style="display:flex;",
        ),
        Hr(),
        Div(
            # Common style for all form rows
            *[
                Div(
                    Div(
                        P(
                            label,
                            style="flex: 0 0 150px; text-align: left; margin-right: 20px; align-self: center; color:black;",
                        ),
                        Div(
                            value,
                            style="flex: 1; height: 30px; padding: 5px 10px; border: 1px solid #ddd; border-radius: 4px;",
                        ),
                        style="display: flex; align-items: center; margin-bottom: 15px; gap: 10px;",
                    )
                )
                for label, value in [
                    ("E-mail:", account.email),
                    ("Name:", account.name),
                    ("Tel:", account.tel),
                    ("Country:", account.location.country),
                    ("Street Address:", account.location.street_address),
                    ("Apt, suite, etc.:", account.location.apt),
                    ("Suburb:", account.location.suburb),
                    ("City:", account.location.city),
                    ("Province:", account.location.province),
                    ("Postal Code:", account.location.postal_code),
                ]
            ],
            password_no_popup_component(),
            style="max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border-radius: 8px;",
        ),
        id="main-content",
    )


def edit_account_details_component():
    account = get_account()
    return Div(
        Div(
            H2("Account Details", style="text-align:left;color:inherit;"),
            Img(
                src="./image/edit.png",
                style="width: 30px; height: 30px; cursor: pointer;margin-left:10px;",
                hx_get="/account-details-back-from-edit",
                hx_target="#main-content",
            ),
            style="display:flex;",
        ),
        Hr(),
        Form(
            # Common style for all form rows
            *[
                Div(
                    Div(
                        P(
                            label,
                            style="flex: 0 0 150px; text-align: left; margin-right: 20px; align-self: center; color:black;",
                        ),
                        Input(
                            value=value,
                            id=field_id,
                            name=field_name,
                            style="flex: 1; height: 30px; border: 1px solid #ddd; border-radius: 4px;",
                        ),
                        style="display: flex; align-items: center; margin-bottom: 15px; gap: 10px;",
                    )
                )
                for label, value, field_id, field_name in [
                    ("E-mail:", account.email, "email", "email"),
                    ("Name:", account.name, "name", "name"),
                    ("Tel:", account.tel, "tel", "tel"),
                    ("Country:", account.location.country, "country", "country"),
                    (
                        "Street Address:",
                        account.location.street_address,
                        "street_address",
                        "street_address",
                    ),
                    ("Apt, suite, etc.:", account.location.apt, "apt", "apt"),
                    ("Suburb:", account.location.suburb, "suburb", "suburb"),
                    ("City:", account.location.city, "city", "city"),
                    (
                        "Province:",
                        account.location.province,
                        "province",
                        "province",
                    ),
                    (
                        "Postal Code:",
                        account.location.postal_code,
                        "postal_code",
                        "postal_code",
                    ),
                ]
            ],
            Div(
                Button(
                    "Save Changes",
                    type="submit",
                    style="padding: 10px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;",
                ),
                style="margin-top: 30px; display: flex; justify-content: flex-end;",
            ),
            style="max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border-radius: 8px;",
            action="/account-details-save-changes",
            method="post",
        ),
        style="background-color: white; min-height: 100vh;",
    )


def display_order_history_component():
    account = get_account()
    order_history = account.order_history
    return (
        Div(
            H2("View Orders", style="text-align:left;color:inherit;"),
            style="display:flex;",
        ),
        Hr(),
        Table(
            Tr(
                Th(
                    "Order ID",
                    style="text-align:center;background-color:white;color:black;",
                ),
                Th(
                    "Product Name",
                    style="text-align:center;background-color:white;color:black;",
                ),
                Th(
                    "Date Purchased",
                    style="text-align:center;background-color:white;color:black;",
                ),
                Th("", style="text-align:center;background-color:white;color:black;"),
            ),
            *chain.from_iterable(
                        [Tr(
                            Td(
                                order.id,
                                style="text-align:center;background-color:white;color:black;",
                            ),
                            Td(
                                course.title,
                                style="text-align:center;background-color:white;color:black;",
                            ),
                            Td(
                                order.payment_detail.time,
                                style="text-align:center;background-color:white;color:black;",
                            ),
                            Td(
                                A(
                                    "View Info",
                                    style="text-align:center; background-color:white",
                                    href=f"/orders&order_id={order.id}&course_id={course.id}",
                                ),
                                style="text-align:center; background-color:white",
                            ),
                        ) for course in order.course
                    ] 
                    for order in sorted(order_history, key=lambda order: order.id, reverse=True)
                ),
        ),
    )


def display_order_info_component(order, course):
    return (
        Div(
            H2(  # display order id in element according to url id
                f"Course ID {course.id} - {course.title}",
                style="text-align:left;color:inherit;",
            ),
            style="display:flex;",
        ),
        Hr(),
        Table(
            Tr(
                Th(
                    "Delivery Detail:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    Span(
                        order.order_status,
                        
                        style="background-color:#d4edda; color:green; padding:5px 10px; border-radius:10px;" if order.order_status == "Accepted" 
                        else "background-color:#f8d7da; color:red; padding:5px 10px; border-radius:10px;" 
                        
                    ),
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            Tr(
                Th(
                    "Order ID:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    order.id,
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            Tr(
                Th(
                    "Order Date:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    order.payment_detail.time,
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            Tr(
                Th(
                    "Purchase Method:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    order.payment_detail.type,
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            Tr(
                Th(
                    "Total:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    f"{order.total_money} THB",
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            Tr(
                Th(
                    "Address:",
                    style="text-align:left;background-color:white;color:black;",
                ),
                Td(
                    f"{order.location.city}, {order.location.province}, {order.location.postal_code}, {order.location.country}",
                    style="text-align:center; background-color:white;color:black;",
                ),
            ),
            style="width:100%; border-collapse:collapse;",
        ),
    )


def setup_routes(rt):
    @rt("/open-account-dropdown")
    def open_account_dropdown():
        if get_account() is None:
            return Response(status_code=200, headers={"HX-Location": "/login"})
        return opened_account_dropdown()

    @rt("/close-account-dropdown")
    def close_account_dropdown():
        return closed_account_dropdown()
