from fasthtml.common import *
from fastapi import FastAPI, Request, Form, status
import Component
import Data
import page_account_details as page_account_details

app, rt = fast_app()

####### common menu route
@rt("/go-to-account-details")
def get():
    return RedirectResponse(url="/account-details", status_code=status.HTTP_303_SEE_OTHER)

####### account details page
@rt("/account-details")
def get():
    return page_account_details.account_details_page()


@rt("/account-details-edit")
def get():
    return Component.edit_data_component()


@rt("/account-details-back-from-edit")
def get():
    return Component.display_data_component()


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
    Data.account.edit_data(
        email,
        name,
        tel,
        [country, street_address, apt, suburb, city, province, postal_code],
    )
    return RedirectResponse(
        url="/account-details", status_code=status.HTTP_303_SEE_OTHER
    )


#######

serve()
