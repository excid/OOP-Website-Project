from fasthtml.common import *
from controller import *
from component import *


def setup_routes(rt):
    @rt('/course/view_video')
    def get(request):
        video_id = request.query_params.get("video_id") if request.query_params.get("video_id") else 0
        course_id = request.query_params.get("course_id")
        accessed_course(course_id) if course_id else None
        video = get_all_video()
        quiz = get_all_quiz()
        selected_video = next((v for v in video if str(v.id) == video_id), None)
        
        
        #prev_video = video[current_index - 1].id if current_index > 0 else None
        #next_video  = video[current_index + 1].id if current_index < len(video) else None
        return Div(
            navbar_component(),
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
                        *[Li(A(Card(f"{vids.title}", style="background-color: #DE4040; box-shadow: 2px 1px; border: 2px; border-color: black"), href=f"/course/view_video/?video_id={vids.id}", cls="button")) for vids in video],
                        *[Li(A(Card(f"{quizs.title}",style="background-color: #90D5FF;"), href=f"/course/quiz?exam_id={quizs.id}", cls="button")) for quizs in quiz]
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
                            src="https://fastcdn.hoyoverse.com/content-v2/hk4e/113484/1a0e331a984e482f84433eac47cd5e3b_3213742424298282717.jpg", style="width: 100%;"
                        ),
                    ),
                    Div(
                        A(Button("Previous", style="float: left;"), href=f"/course/view_video/?video_id={int(video_id) - 1 if int(video_id) > 0 else len(video) - 1}"),
                        A(Button("Next", style="float: right;"), href=f"/course/view_video/?video_id={int(video_id) + 1 if int(video_id) <= len(video) - 1 else 1}"),
                        style="padding: 20px; text-align: center;"
                    ),
                    style="flex-grow: 1; padding: 10px; background-color: #f0f0f0;"
                ),
                style="display: flex; height: 100%;"
            ),

            style="margin: 0px;background-color: white; min-height: 100vh; width: 100vw; color: black; display: flex; flex-direction: column;"
        )