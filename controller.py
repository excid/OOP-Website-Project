from database import *

def get_account_course(account_id):
    print("this is account id", account_id)
    account = app.search_account(account_id)
    return account.course

def get_all_course():
    return app.course

def get_all_video(course_id):
    print(course_id)
    course = app.search_course(course_id)
    return course.video

def get_exam(course_id, exam_id, account_id):
    account = app.search_account(account_id)
    course = account.search_course(course_id)
    exam = course.search_exam(exam_id)
    return exam
    
def get_all_quiz(course_id):
    course = app.search_course(course_id)
    print(course.exam)
    return course.exam

def grading(form_data, exam):
    for item in exam.items:
            try:
                choice = form_data[f"q{item.number}"]  # Access user's choice for each question
                if choice == item.answer:
                    exam.score += 1
            except:
                pass