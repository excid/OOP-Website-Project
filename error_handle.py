from fasthtml.common import *

def setup_route(rt):
    @rt('/de-access')
    def get():
        return Div(
            H1("Access Denied"),
            P("You do not have permission to access this page."), 
            A("Go back to home", href="/", style="text-align: center; padding-top: 50px; font-size: 50px;"),
            style="text-align: center; padding-top: 50px; font-size: 50px;"
        )