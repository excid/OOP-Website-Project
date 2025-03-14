from fasthtml.common import *
from component import navbar_component
from controller import get_all_course, add_to_cart, get_account



def homepage():
    return Div(
        navbar_component(),
        Img(src="./image/cover.png", style="width: 100vw; height: auto;"),
        hero_section(),
        hot_selling_courses(),
        Div("© No copyrights as of now, as a part of OOP project.",
            style="text-align: center; padding: 10px; font-size: 10px; color: #333;"
            ),
        style="width:100%; min-height: 100vh; background-color:white; color:black;",
    )


def Tag(name):
    return Span(
        name,
        style="background-color: #eee; padding: 3px 8px; border-radius: 8px; font-size: 12px; -webkit-user-select: none; -ms-user-select: none; user-select: none;",
    )


def course_card(course):
    return (
        Card(
            Div(
                Img(
                    src=course.img,
                    style="width:250px; height:250px;margin:auto;",
                ),
                Style="background-color: #efefef;display: grid; place-items: center; text-align: center; padding: 15px;",
            ),
            H3(
                course.title,
                Style="text-align: left;color : black;text-align: center; font-size:18px;",
            ),
            H6(
                f"Course ID: {course.id} - Price: {course.price} THB",
                style="text-align: center;",
            ),
            Div(
                Body(
                    A(
                        "ADD TO CART",
                        hx_post=f"/add-to-cart/{course.id}",  # Sends course.id to the backend
                        hx_swap="none",  # No need to update anything on the page
                        cls="button",
                        style="margin-bottom:15px; margin-top:15px; width:250px; font-size:12px; border-radius:15px;"
                    ),
                    Br(),
                    A(
                        "VIEW INFO",
                        cls="button",
                        href=f"/course_info/{course.id}",
                        style="width:250px; font-size:12px; border-radius:15px;"
                        # not yet asdasddone
                    ),
                ),
                Style="text-align: center; margin = auto;",
            ),
            cls="course-card",
            Style="background-color: #efefef; width: 100%; height: 100%;margin: 0; padding:0; padding-bottom:15px;",
        ),
    )


def hero_section():
    return Div(
        Div(
            Div(
                Div(
                    "Welcome!",
                    style="margin-top: -20px; font-weight: 800; font-size: 50px; color:blue",
                ),
                Div(
                    "To CAM'ERA",
                    style="font-weight: 500; font-size: 40px; margin-bottom: 10px;",
                ),
                Div(
                    "A place for online courses and learning. Website created by Computer Engineering Student at King Mongkut's Institute of Technology Ladkrabang.",
                    style="font-weight: 100; font-size: 0.9rem; color: black; margin-bottom: 15px; width: 80%;",
                ),
                Div(
                    A(
                        Button(
                            "SIGN IN",
                            style="margin-top: 10px; background-color: #59A3F9; color: white; font-weight: bold; "
                            "border-radius: 8px; padding: 10px 120px; font-size: 12px;",
                        ),
                        href="/login",
                    ),
                    Br(),
                    A(
                        Button(
                            "SIGN UP",
                            style="margin-top: 15px; background-color: transparent; color: black; font-weight: bold; "
                            "border-radius: 8px; padding: 10px 118px; font-size: 12px; border: 2px solid #59A3F9;",
                        ),
                        href="/signup",
                    ),
                ),
                style="margin-top:40px; padding-left:60px;",
            ),
            Div(
                Div(
                    Video(src="vids/1.polynomial.mp4", controls=True, autoplay=True, style="width: 100%;"),
                    style="width: 100%;",
                ),
                Div(
                    H3("Interesting Topics:", style="color:black;"),
                    Div(
                        Tag("🖥️ Website Development"),
                        Tag("🎮 Game Development"),
                        Tag("📱 Hardware"),
                        Tag("🤖 AI/Machine Learning"),
                        Tag("🌏 Network"),
                        Tag("🚀 Cyber Security"),
                        style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; width:800px",
                    ),
                    style="width: 50%;",
                ),
                style="padding-right:60px;"
            ),
            style="display: flex; color: black; gap: px;",
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh; color:black;",
    )


def hot_selling_courses():
    course = get_all_course()
    return Div(
        
        H2("Hot Selling Course", style="color:black; font-size:20px"),
        Div(
            Body(
                Div(*[course_card(course[i]) for i in range(len(course) -1 if len(course) <=3 else 3)], cls="grid"),
                ),
                Style(
                    ".grid {display:flex; wrap; gap: 15px; padding: 15px;}"
                    ".course-card {padding: 15px; border-radius: 0px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);background-color: #fffff;}"
                    ".button {background-color: #de4040; color: white; padding: 8px 15px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;}"
                    ".button:hover {background-color: auto;}"
                    "a {text-decoration: none; color: white;}"
                    "a:hover {text-decoration: none; color: white;}"
                ),
                Style="background-color: #ffffff; width: 100%; height: 50%;margin: 0; padding: 0;",
            ),
            A(Button(
                "View All Products",
                style="border-radius:0px; background-color: red; color: white; border: none; padding: 8px 15px; margin-top:60px; align-items: center; justify-content: center; font-size:12px;",
                ),href="/course"
              ),
            style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;",
        )


def setup_routes(rt):
    @rt("/")
    def get():
        return homepage()
    
    @rt("/add-to-cart/{course_id}")
    def post(course_id: str):
        if get_account() is None:
            return Response(status_code=200, headers={"HX-Location": "/login"})
        add_to_cart(course_id)  # Call the function to add the course

