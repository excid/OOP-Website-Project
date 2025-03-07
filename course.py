from fasthtml.common import *
from controller import *

video = get_all_video("1")
quiz = get_all_quiz("1")
print(quiz[0].id)
course_id = "1"


def setup_routes(rt):
    @rt('/course')
    def get(request):
        video_id = request.query_params.get("video_id")
        selected_video = next((v for v in video if str(v.id) == video_id), None)
        return Div(
            Card(
                H1("Online Course"),
                P("Python Programming Course"),
                style="background-color: white; color: red; text-align: center;"  # Fixed typo
            ),
            Hr(style="border: 1px solid black;"),
            Div(
                Div(
                    H2("Course Videos"),
                    Ul(
                        *[Li(A(Card(f"{vids.title}", style="background-color: #DE4040; box-shadow: 2px 1px; border: 2px; border-color: black"), href=f"/course/?video_id={vids.id}")) for vids in video],
                        Li(A("6. Quiz", href=f"/quiz?exam_id={quiz[0].id}&course_id={course_id}"))
                    ),
                    style="width: 20%; height: 100vh; padding: 10px; background-color: #f0f0f0;"
                ),
                Div(style="width: 2px; background-color: gray; height: 100vh;"),  # Full height
                Container(
                    H2("Course Content", style="text-align: center;"),
                    Container(
                        ft("video",
                            ft("source", src=selected_video.path if selected_video else "", type="video/mp4"),
                            controls="true",
                            autoplay="true",
                            loop="true",
                            muted="true",
                            width="100%",
                        ) if selected_video else Img(
                            src="https://fastcdn.hoyoverse.com/content-v2/hk4e/113484/1a0e331a984e482f84433eac47cd5e3b_3213742424298282717.jpg"
                        ),
                    ),
                    Div(
                        Button("Previous", style="float: left;"),
                        Button("Next", style="float: right;"),
                        style="padding: 20px; text-align: center;"
                    ),
                    style="flex-grow: 1; padding: 10px; background-color: #f0f0f0;"
                ),
                style="display: flex; height: 100vh;"
            ),

            style="margin: 0px;background-color: white; min-height: 100%; width: 100vw; color: black; display: flex; flex-direction: column;"
        )
        
    @rt("/course/display")
    def post_display():
        return Div(H1("Quiz Page"), id="quiz-container")