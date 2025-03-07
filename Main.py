from fasthtml.common import *
from quiz import setup_routes as setup_quiz_routes
from course import setup_routes as setup_course_routes
#from Account_detail import setup_routes as setup_Account_routes
from account_details import setup_routes as setup_account_details_routes
from order_history import setup_routes as setup_order_history_routes
from database import *
from dataclasses import *
from typing import List

# Initialize FastHTML app
app, rt = fast_app()

# Register routes from quiz.py and course.py
setup_quiz_routes(rt)
setup_course_routes(rt)
#setup_Account_routes(rt)
setup_account_details_routes(rt)
setup_order_history_routes(rt)

# Run the server
serve()