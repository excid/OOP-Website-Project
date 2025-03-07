from fasthtml.common import *
from database import account, order_history

def display_account_details_component():
    return (
        Div(
            Div(
                H2("Account Details", style="text-align:left;color:inherit;"),
                Img(
                    src="./image/edit.png",
                    style="width: 30px; height: 30px; border-radius: 50%; cursor: pointer;",
                    hx_get="/account-details-edit",
                    hx_target="#main-content",
                ),
                style="display:flex;",
            ),
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
                style="max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border-radius: 8px;",
            ),
            id="main-content",
        ),
    )


def edit_account_details_component():
    return Div(
        Div(
            H2("Account Details", style="text-align:left;color:inherit;"),
            Img(
                src="./image/edit.png",
                style="width: 30px; height: 30px; border-radius: 50%; cursor: pointer;",
                hx_get="/account-details-back-from-edit",
                hx_target="#main-content",
            ),
            style="display:flex;",
        ),
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
    return (
        Div(
            H2("View Orders", style="text-align:left;color:inherit;"),
            style="display:flex;",
        ),
        Hr(),
        Table(
            Tr(
                Th("Order ID",style="text-align:center;"),
                Th("Product Name",style="text-align:center;"),
                Th("Date Purchased",style="text-align:center;"),
                Th(""),
            ),
            *[Tr(
                Td(order.id,style="text-align:center;"),
                Td(order.course.title,style="text-align:center;"),
                Td(order.datetime,style="text-align:center;"),
                Td("View Info",style="text-align:center;"),
            )
            for order in order_history],
        )
    )