from fasthtml.common import *
from mycart import setup_routes as mycart_routes
from database import *
from billing import setup_routes as billing_routes
app, rt = fast_app()
mycart_routes(rt)
billing_routes(rt)
serve()