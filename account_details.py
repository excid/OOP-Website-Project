# account_details.py
from fasthtml.common import *
from fastapi import FastAPI, Request, Form, status
import component
from controller import *


def account_details_page():
    # Render the account details
    if get_account() is None:
        return RedirectResponse(url="/login")
    
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
                A(Button(
                    "Logout",
                    
                    style="text-align:left; color:red; background: transparent; border: none; cursor: pointer; height:45px; width:100%; outline: none;",
                )
                  ,href="/logout"),
                Hr(style="width:100%;text-align:left;margin-left:0;"),
                style="width: 25%; min-width: 200px; padding: 20px; border-right: 1px solid #ccc;",
            ),
            # Account Details (Right Side) - Aligned to the Left
            Div(
                component.display_account_details_component(),
                style="width: 75%; padding: 20px; text-align:left;",
            ),
            # Apply Flexbox
            style="display: flex; width: 100%;",
        ),
        style="width:100%; min-height: 100vh; background-color:white; color:black;",
    )


def setup_routes(rt):
    ####### account details page
    @rt("/account-details")
    def get():
        return account_details_page()

    @rt("/account-details-edit")
    def get():
        return component.edit_account_details_component()

    @rt("/account-details-back-from-edit")
    def get():
        return component.display_account_details_component()

    @rt("/change-password")
    def get():
        return component.change_password_component()

    @rt("/back-from-change-password")
    def get():
        return component.password_no_popup_component()

    @rt("/change-password-submit")
    def post(
        new_password: str = Form(...),
        confirm_password: str = Form(...),
    ):


        # Update the password in the account object
        

        change_password(new_password, confirm_password)

        return RedirectResponse(
            url="/account-details", status_code=status.HTTP_303_SEE_OTHER
        )

    @rt("/account-details-save-changes")
    def post(
        email: str,
        name: str,
        tel: str,
        country: str,
        street_address: str,
        apt: str,
        suburb: str,
        city: str,
        province: str,
        postal_code: str,
    ):
        edit_account_data(email,name,tel,[country, street_address, apt, suburb, city, province, postal_code],)
        
        
        return RedirectResponse(
            url="/account-details", status_code=status.HTTP_303_SEE_OTHER
        )
        
    @rt("/logout")
    def post():
        logout()
        return RedirectResponse(url="/login")
