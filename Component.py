from fasthtml.common import *

def display_data_component():
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
                        ("E-mail:", Data.account.email),
                        ("Name:", Data.account.name),
                        ("Tel:", Data.account.tel),
                        ("Country:", Data.account.location.country),
                        ("Street Address:", Data.account.location.street_address),
                        ("Apt, suite, etc.:", Data.account.location.apt),
                        ("Suburb:", Data.account.location.suburb),
                        ("City:", Data.account.location.city),
                        ("Province:", Data.account.location.province),
                        ("Postal Code:", Data.account.location.postal_code),
                    ]
                ],
                style="max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border-radius: 8px;",
            ),
            id="main-content",
        ),
    )


def edit_data_component():
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
                    ("E-mail:", Data.account.email, "email", "email"),
                    ("Name:", Data.account.name, "name", "name"),
                    ("Tel:", Data.account.tel, "tel", "tel"),
                    ("Country:", Data.account.location.country, "country", "country"),
                    (
                        "Street Address:",
                        Data.account.location.street_address,
                        "street_address",
                        "street_address",
                    ),
                    ("Apt, suite, etc.:", Data.account.location.apt, "apt", "apt"),
                    ("Suburb:", Data.account.location.suburb, "suburb", "suburb"),
                    ("City:", Data.account.location.city, "city", "city"),
                    (
                        "Province:",
                        Data.account.location.province,
                        "province",
                        "province",
                    ),
                    (
                        "Postal Code:",
                        Data.account.location.postal_code,
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
