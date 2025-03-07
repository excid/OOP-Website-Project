from fasthtml.common import *
from dataclasses import dataclass
from typing import List
from controller import get_account_course


def setup_routes(rt):
    @rt('/course')
    def course_get(request):
        search_form = Form(
                             Label(
                                    Input(type="search", placeholder="search", cls="search"),
                                    cls="search-container",
                                    style="background-color: #ffffff; weigth: 20vh;"
                                ),
                            hx_get="/search", hx_target="#search-results", hx_trigger="submit"
                        )

        #account_id =  request.query_params.get("account_id")
        account_id = "1"
        courses = get_account_course(account_id)
        return Container(
                    Header( 
                            Header( 
                                Div(
                                    Div(
                                        H1("My Course", style="color: black; font-weight: bold; margin: 0; position: absolute; left: 50%; transform: translateX(-50%);"),
                                        search_form,
                                        style="display: flex; align-items: center; width: 100%; position: relative;"
                                    ),
                                    style="display: flex; justify-content: flex-end; align-items: center; width: 100%; padding: 10px;"
                                ),
                            ),
                        H6("view aviailable courses here",style="text-align: center;color: black; font-weight: thin;"),
                        Hr(),
                        Br(),
                            
                    ),

                    Body(
                        Div(
                            *[
                                Card(
                                    Div(
                                        Img(src=course.img, alt=f"{course.title} Image", style="width:300px; height:300px;margin:auto;"),
                                        Style = "background-color: #efefef;display: grid; place-items: center; text-align: center; padding: 20px;",
                                    ),  

                                    H3(course.title,Style="text-align: left;color : black;text-align: center;"),
                                    H6(f"Course Progression : {course.progress}%",style="text-align: center;"),
                                    Progress(value=course.progress, max=100, style="width: 80%; height: 8px; border-radius: 5px; display: block; margin: auto; margin-bottom: 10px"),
                                    Div(   
                                        H5(
                                            A("VIEW INFO", href=f"/course/course_info/?course_id={course.id}", cls="button"),"\t",
                                            A("Continue", href=f"/course/view_video/?course_id={course.id}&account_id={account_id}", cls="button")
                                        ),
                                        Style="text-align: center;margin = auto;"
                                    ),
                                    cls="course-card",

                                    Style = "background-color: #efefef; width: 100%; height: 100%;margin: 0; padding:0;",
                                ) for course in courses
                            ], cls="grid"
                        ),

                        Style(".grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 20px;}"
                            ".course-card {padding: 20px; border-radius: 0px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);background-color: #fffff;}"
                            ".button {background-color: #de4040; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;}"
                            ".button:hover {background-color: auto;}"
                            "a {text-decoration: none; color: white;}"
                            "a:hover {text-decoration: none; color: white;}"
                        ),

                        Style = "background-color: #ffffff; width: 100%; height: 100%;margin: 0; padding: 0;"

                    ),

                    Style = "background-color: white; width: 100%; height: 100%;margin: center; padding: 0;"

                )



