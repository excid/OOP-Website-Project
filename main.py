from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get():
    return Div(
        Header(""),
        style="""
        width:100;
        min-height: 100vh;
        background-color:white;
        """
    )
    

serve()