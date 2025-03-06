from fasthtml.common import fast_app, serve
from quiz import setup_routes as setup_quiz_routes, exam
from course import setup_routes as setup_course_routes
from Account_detail import setup_routes as setup_Account_routes
from database import *
from dataclasses import *
from typing import List

# Initialize FastHTML app
app, rt = fast_app()

# Register routes from quiz.py and course.py
setup_quiz_routes(rt)
setup_course_routes(rt)
setup_Account_routes(rt)

# Run the server
serve()