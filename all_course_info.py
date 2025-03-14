from fasthtml.common import *
from controller import *
from component import *

def setup_routes(rt):
    all_course = get_all_course()
    @rt("/course")
    def get():
        # Search Form
        search_form = Form(
            Div(
                Input(type="search", placeholder="search", cls="search"),
                cls="search-container",
                style="background-color: white;color: black;"
            ),
            hx_get="/search", hx_target="#search-results", hx_trigger="submit"
        )

        return Div(
        Header( navbar_component(),
            Br(),
            Div(
                H1(".............................",style="color: white; "),
                H1("Course", style="color: black; font-weight: bold; margin: auto;text-align: center;"),
                search_form,
                style="display: flex; justify-content: space-between; align-items: center; width: 100%;high: 70%;"
            ),
            Div(
                H6("View our available courses here", style="text-align: center; color: black; font-weight: thin; margin: auto;"),
                style="text-align: center; width: 100%;"
            ),
            Br(),
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
                            H6(f"course id : {course.id}","\t"f"Price    : {course.price}",style="text-align: center;"),
                            Div(   
                                H5(
                                    A("VIEW INFO", href=f"/course_info/{course.id}", cls="button"),"\t",
                                    A("ADD TO CART", hx_post=f"/add-to-cart/{course.id}", hx_swap="none", cls="button")
                                ),
                                Style="text-align: center;margin = auto;"
                            ),
                            cls="course-card",

                            Style = "background-color: #efefef; width: 100%; height: 100%;margin: 0; padding:0;",
                        ) for course in all_course
                    ], cls="grid"
                ),

                Style(
                        ".grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 20px;}"
                        ".course-card {padding: 20px; border-radius: 0px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #ffffff;}"
                        ".button {background-color: white; color: black; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;}"
                        ".button:hover {background-color: #de4040;}"
                        "a {text-decoration: none; color: black;}"
                        "a:hover {text-decoration: none; color: white;}"
                ),
                Style = "background-color: #ffffff; width: 100%; height: 100%;margin: 0; padding: 0;"

            ),

            Style = "background-color: white; width: 100%; height: 100%;margin: center; padding: 0;"

        )

    # Course info page
    @rt("/course_info/{course_id:str}")
    def get(course_id: str):
        course = get_course(course_id)
        if not course:
            return H1("Course not found")

        return Div(navbar_component(),
            Header(
                H1("Course Information", style="text-align: center; color: black; font-weight: bold;"),
                H6(course.id, "-", course.title, style="text-align: center; color: black; font-weight: bold;"),
                Hr(),
            ),
            Body(
                Div(
                    Img(src=course.img, alt=f"{course.title} Image", style="width:400px; height:auto; margin:auto;"),
                    style="text-align: center; padding: auto; margin: auto;border-radius: 20px;",
                ),
                Div(
                    Div(H2(B("Course Detail: ")), H4(course.detail, style="color: black;"), Br(), cls="section"),
                    Div(H2(B("Course Price: ")), H4(course.price, style="color: black;"), Br(), cls="section"),
                    style="background-color: #ffffff; color: black; padding: 20px;"
                ),
                Div(
                    A("⬅ Back to Courses", href="/course", cls="button", style="margin-right: 20px; color: black;"),
                    Span(style="border-left: 1px solid black; height: 80px; margin-right: 20px;"),
                    ###########################################ดึงไปหน้าcart################################################
                    A("Add to Cart", hx_post=f"/add-to-cart/{course.id}", cls="button", style="color: black;"),
                    style="background-color: #ffffff; width: 100%; height: 100%; margin: auto; padding: auto; color: black; display: flex-center; align : center;"
                ),
                style="background-color: #ffffff; width: 100%; height: 100%; margin: auto; padding: auto; color: black; align: center;",  
            ),
            Style(
                ".grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 20px;}"
                ".course-card {padding: 20px; border-radius: 0px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #ffffff;}"
                ".button {background-color: white; color: black; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px solid black;}"
                ".button:hover {background-color: #de4040; color: white;}"
                "a {text-decoration: none; color: black;}"
                "a:hover {text-decoration: none; color: white;}"
                "h1, h2, h3, h4, h5, h6, p, span {color: black;}"  
            ),
        )
        
    @rt("/add-to-cart/{course_id}")
    def post(course_id: str):
        add_to_cart(course_id)