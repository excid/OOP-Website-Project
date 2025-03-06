from fasthtml.common import *
import Component
import Data
import page.account_details as account_details 

app, rt = fast_app()

####### account details page
@rt("/account-details")
def get():
    return account_details.account_details_page()

@rt("/edit")
def get():
    return Component.edit_data_component()


@rt("/back-from-edit")
def get():
    return Component.display_data_component()


@rt("/save-changes")
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
    return account_details.account_details_page()
#######

serve()