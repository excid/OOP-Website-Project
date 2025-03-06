from fasthtml.common import *
from dataclasses import *
from controller import *

video = get_all_course()
video = video[0].video
print(app.course)

def setup_routes(rt):
    @rt('/')
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
                        *[Li(A(Card(f"{vids.title}", style="background-color: #DE4040; box-shadow: 2px 1px; border: 2px; border-color: black"), href=f"/?video_id={vids.id}")) for vids in video],
                        Li(A("6. Quiz", href="/quiz"))
                    ),
                    style="width: 20%; padding: 10px; background-color: #f0f0f0;"
                ),
                Div(style="width: 2px; background-color: gray; height: 100vh;"),
                Div(
                    H2("Course Content", style="text-align: center;"),
                    Iframe(
                        src="https://www.youtube.com/watch?v=6rDd9fQKI9A&list=RD6rDd9fQKI9A&start_radio=1",
                        width="600", height="400", frameborder="0",
                        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture",
                        allowfullscreen=True  
                    ) if selected_video else Img(src="https://fastcdn.hoyoverse.com/content-v2/hk4e/113484/1a0e331a984e482f84433eac47cd5e3b_3213742424298282717.jpg"),
                    Div(
                        Button("Previous", style="float: left;"),
                        Button("Next", style="float: right;"),
                        style="margin: 40px; text-align: center;"
                    ),
                    style="width: 100%; padding: 10px; background-color: #f0f0f0;"
                ),
                style="display: flex; height: 100vh;"
            ),
            style="background-color: white; height: 100vh; width: 100vw; color: black; display: flex; flex-direction: column;"
        )