from fasthtml.common import *
from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    done: bool
    number: int
    question: str
    answer: str
    choices: List[str]
    correctness: bool

@dataclass
class Exam:
    title: str
    items: List[Item]
    score: int = 0

def setup_routes(rt):
    @rt('/quiz')
    def quiz_get():
        print("Quiz route accessed")  # Debug statement
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
    def submit_post(request):
        for item in exam.items:
            choice = request.form[f"q{item.number}"]
            if choice == item.answer:
                item.correctness = True
                exam.score += 1
            else:
                item.correctness = False
        return RedirectResponse("/result")

    @rt('/result')
    def result_get():
        return Div(
                H1("Result"),
                H3(f"Your score is {exam.score}"),
                style="items-aligh: center;"
            )

def set_exam():
    return Exam("Python Programming Quiz", [
        Item(False, 1, "What is the output of 2 + 2?", "4", ["2", "3", "4", "5"], False),
        Item(False, 2, "What is the output of 2 * 2?", "4", ["2", "3", "4", "5"], False),
        Item(False, 3, "What is the output of 2 / 2?", "1", ["0", "1", "2", "3"], False),
        Item(False, 4, "What is the output of 2 - 2?", "0", ["0", "1", "2", "3"], False),
        Item(False, 5, "What is the output of 2 ** 2?", "4", ["2", "3", "4", "5"], False),
    ])

exam = set_exam()