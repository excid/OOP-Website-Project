from fasthtml.common import *
from quiz import setup_routes as setup_quiz_routes
from view_video import setup_routes as setup_view_video_routes
from my_course import setup_routes as setup_course_routes
from account_details import setup_routes as setup_account_details_routes
from order_history import setup_routes as setup_order_history_routes
from component import setup_routes as drop_down_routes
from order_info import setup_routes as setup_order_info_routes
from home import setup_routes as setup_home_routes
from mycart import setup_routes as setup_mycart_routes
from billing import setup_routes as setup_billing_routes
from login import setup_routes as setup_login_routes
from all_course_info import setup_routes as setup_all_course_info_routes

from database import *
from dataclasses import *
from typing import List

# Initialize FastHTML app
app, rt = fast_app()

# Register routes from quiz.py and course.py
setup_all_course_info_routes(rt)
setup_login_routes(rt)
setup_billing_routes(rt)
setup_mycart_routes(rt)
setup_home_routes(rt)
setup_quiz_routes(rt)
setup_view_video_routes(rt)
setup_course_routes(rt)
setup_account_details_routes(rt)
setup_order_history_routes(rt)
drop_down_routes(rt)
setup_order_info_routes(rt)
#setup_Account_routes(rt)
#setup_account_details_routes(rt)
#setup_order_history_routes(rt)

# Run the server
serve()