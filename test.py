from fasthtml.common import *
from component import navbar_component
from controller import *
course = get_course("1")

app, rt = fast_app()

def homepage():
    return Div(
        navbar_component(),
        Img(src="./image/cover.png", style="width: 100%; height: auto;"),
        hero_section(),
        hot_selling_courses(),
        Div("© No copyrights as of now, as a part of OOP project.",
            style="text-align: center; padding: 1%; font-size: 0.9em; color: #333;"
            ),
        style="width: 100%; min-height: 100vh; background-color: white; color: black;",
    )

def Tag(name):
    return Span(
        name,
        style="background-color: #eee; padding: 0.5% 1%; border-radius: 8px; font-size: 0.9em; -webkit-user-select: none; -ms-user-select: none; user-select: none; margin-top:2%;",
    )

def course_card(course):
    return (
        Card(
            Div(
                Img(
                    #src="./image/logo.png",
                    alt="Image",
                    style="width: 100%; height: auto; margin: auto;",
                ),
                Style="background-color: #efefef; display: grid; place-items: center; text-align: center; padding: 2%;",
            ),
            H3(
                course.title,
                Style="text-align: left; color: black; text-align: center; font-size: 1.2em;",
            ),
            H6(
                f"Course ID: {course.id} - Price: {course.price} THB",
                style="text-align: center;",
            ),
            Div(
                Body(
                    A(
                        "ADD TO CART",
                        cls="button",
                        style="margin-bottom: 2%; margin-top: 2%; width: 100%; font-size: 0.9em; border-radius: 15px;"
                    ),
                    Br(),
                    A(
                        "VIEW INFO",
                        cls="button",
                        style="width: 100%; font-size: 0.9em; border-radius: 15px;"
                    ),
                ),
                Style="text-align: center; margin: auto;",
            ),
            cls="course-card",
            Style="background-color: #efefef; width:50%; height: 50%; margin: 0; padding: 0; padding-bottom: 2%;",
        ),
    )

def hero_section():
    return Div(
        Div(
            Div(
                Div(
                    "Welcome!",
                    style="margin-top: -2%; font-weight: 800; font-size: 5em; color: blue;",
                ),
                Div(
                    "To borntoDie",
                    style="font-weight: 500; font-size: 3em; margin-bottom: 1%;",
                ),
                Div(
                    "A place for online courses and learning.",
                    Br(),
                    "Website created by Computer Engineering Student at King Mongkut's Institute of Technology Ladkrabang.",
                    style="font-weight: 100; font-size: 1em; color: black; margin-bottom: 2%; width: 80%;",
                ),
                Div(
                    A(
                        Button(
                            "SIGN IN",
                            style="margin-top: 1%; background-color: #59A3F9; color: white; font-weight: bold; border-radius: 8px; padding: 1% 35%; font-size: 0.9em;",
                        ),
                        href="signin",
                    ),
                    Br(),
                    A(
                        Button(
                            "SIGN UP",
                            style="margin-top: 1.5%; background-color: transparent; color: black; font-weight: bold; border-radius: 8px; padding: 1% 34.5%; font-size: 0.9em; border: 2px solid #59A3F9;",
                        ),
                        href="signup",
                    ),
                ),
                style=" padding-left: 10%; width: 100%;",
            ),
            Div(
                Div(
                    Video(src="video.mp4", controls=True, style="width: 160%;"),
                    style="width: 100%;",
                ),
                Div(
                    H3("Interesting Topics:", style="color: black;"),
                    Div(
                        Tag("🖥️ Website Development"),
                        Tag("🎮 Game Development"),
                        Tag("📱 Hardware"),
                        Tag("🤖 AI/Machine Learning"),
                        Tag("🌏 Network"),
                        Tag("🚀 Cyber Security"),
                        style="display: flex; flex-wrap: wrap; gap: 2%; margin-top: 1%; width: 170%;",
                    ),
                    style="width: 100%; padding-top:10%",
                ),
                style="padding-right: 20%;"
            ),
            style="display: flex; color: black;",
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh; color: black;",
    )

def hot_selling_courses():
    return Div(
        H2("Hot Selling Course", style="color: black; margin-left: 5%; font-size: 1.5em;"),
        Div(
            Body(
                Div(
                    course_card(course),
                    course_card(course),
                    course_card(course),
                    cls="grid",
                ),
                Style(
                    ".grid {display: flex;}"
                    ".course-card {padding: 2%; border-radius: 0px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #ffffff;}"
                    ".button {background-color: #de4040; color: white; padding: 1% 2%; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;}"
                    ".button:hover {background-color: auto;}"
                    "a {text-decoration: none; color: white;}"
                    "a:hover {text-decoration: none; color: white;}"
                ),
                Style="background-color: #ffffff; width: 100%; height: 100%; margin: 0; padding: 0;",
            ),
            Button(
                "View All Products",
                style="border-radius: 0px; background-color: red; color: white; border: none; padding: 1% 2%; margin-top: 2%; align-items: center; justify-content: center; font-size: 0.9em;",
            ),
            style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh;",
        ),
    )


@rt("/")
def get():
    return homepage()

serve()