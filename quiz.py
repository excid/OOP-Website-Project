from fasthtml.common import *
from dataclasses import dataclass
from typing import List
from controller import get_exam, grading

def setup_routes(rt):
    @rt('/quiz')
    def quiz_get(request):
        global exam
        print("Quiz route accessed")
        course_id = request.query_params.get("course_id")
        exam_id = request.query_params.get("exam_id")
        print(course_id, exam_id)
        exam = get_exam(course_id, exam_id)
        
        return Div(
            Div(
                H1("Quiz"),
                H3(f"{exam.title}"),
                style="text-align: center; padding-top: 50px; font-size: 50px;"  # Fixed typo
            ),
            Hr(style="border: 2px solid black;"),
            Form(
                *[Div(
                    H3(f"Question number {item.number} : {item.question}"),
                    *[Label(Input(type="radio", name=f"q{item.number}", value=choice), choice, style="padding-left: 40px;") for choice in item.choices],
                    Hr(),
                    style="padding-top: 20px;"
                ) for item in exam.items],
                Button("Submit", style="padding-left: 150px; padding-right: 150px; float: right;"),
                action="/submit",
                method="post"
            ),
            style="padding-left: 100px; margin-bottom: 150px;"
        )

    @rt('/submit')
    async def submit_post(request):  # Make the function asynchronous
        global exam
        if not exam:
            return Div("Exam not found. Please start the quiz again.")
        form_data = await request.form()  # Use await to get form data
        
        # Grade the exam
        
        grading(form_data, exam)
        
        return RedirectResponse("/result")

    @rt('/result')
    def result_get():
        global exam
        return Div(
                H1("Result"),
                H3(f"Your score is {exam.score}"),
                style="items-aligh: center;"
            )

