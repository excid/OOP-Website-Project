from fasthtml.common import *
from dataclasses import dataclass
from typing import List
from controller import get_exam, grading

def setup_routes(rt):
    @rt('/course/quiz')
    def quiz_get(request):
        global exam
        exam_id = request.query_params.get("exam_id")
        print(exam_id)
        exam = get_exam(exam_id)
        
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
                action="/course/quiz/submit",
                method="post"
            ),
            style="padding-left: 100px; margin-bottom: 150px;"
        )

    @rt('/course/quiz/submit')
    async def submit_post(request):  # Make the function asynchronous
        global exam
        if not exam:
            return Div("Exam not found. Please start the quiz again.")
        form_data = await request.form()  # Use await to get form data
        
        # Grade the exam
        
        grading(form_data, exam)
        
        return RedirectResponse("/course/quiz/result")

    @rt('/course/quiz/result')
    def result_get():
        global exam
        return Container(
            Div(
                H1("Quiz Result", style="color: #333; font-size: 2.5rem; font-weight: bold; text-align: center;"),
                H3(f"Your score is {exam.score}", style="color: #007BFF; font-size: 2rem; text-align: center;"),

                Br(),  # Adds spacing

                # Back button
                Div(
                    A("⬅ Back to Course", href="/course/view_video", 
                    style="display: inline-block; padding: 12px 24px; background-color: #de4040; color: white; text-decoration: none; border-radius: 5px; font-size: 1rem;"),
                    style="text-align: center; margin-top: 20px;"
                ),

                style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;"
            )
        )


