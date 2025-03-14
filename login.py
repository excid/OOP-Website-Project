from fasthtml.common import *
from controller import *
from component import navbar_component    # Define the Course class


def setup_routes(rt):
    @rt("/login")
    def get():
        return Div(navbar_component(),
            Header(
                H1("Login", style="text-align: center;color: black;"),
                H6("Login to your account", style="text-align: center; color: black; font-weight: thin;"),
                Hr(), Br(),
            ),
            Body(
                Div(
                    Card(
                        Form(
                            Label("Username or Email", style="font-weight: bold;color : black;"),
                            Input(type="text", name="username", placeholder="Enter your username or email", required=True),
                            Label("Password", style="font-weight: bold;color : black;"),
                            Input(type="password", name="password", placeholder="Enter your password", required=True),

                            # ✅ FIXED: Ensure button posts correctly
                            Button("Login", type="submit", cls="button",
                                hx_post="/logins", hx_target="#login-status",
                                style="width: 100%; background-color: #de4040; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;"),
                            
                            A("Don't have an account? Sign up here", href="/signup",
                            style="display: block; text-align: center; margin-top: 10px; color: #007bff; text-decoration: none;"),
                            Div(id="login-status", style="margin-top: 10px; color: red; text-align: center;"),  # ✅ Feedback area
                            style="padding: 20px;background-color: #ffffff;",
                        ),
                        id="login-form",
                        style="max-width: 600px; margin: auto; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px;background-color: #ffffff;",
                    ),
                    style="background-color: #ffffff;",
                )
            )
        )


    @rt("/signup")
    def get():
        return Div(navbar_component(),
            Header(
                H1("Sign Up", style="text-align: center; color: black;"),
                H6("Create an account to get started", style="text-align: center; color: black; font-weight: thin;"),
                Hr(), Br(),
            ),
            Body(
                Div(
                    Card(
                        Form(
                            Div(
                                Div(
                                    Label("First Name", style="font-weight: bold; color: black;"),
                                    Input(type="text", name="first_name", placeholder="Enter your first name", required=True, style="width: 95%;"),
                                    style="flex: 1; margin-right: 10px;",  
                                ),
                                Div(
                                    Label("Last Name", style="font-weight: bold; color: black;"),
                                    Input(type="text", name="last_name", placeholder="Enter your last name", required=True, style="width: 95%;"),
                                    style="flex: 1;",  
                                ),
                                style="display: flex;", 
                            ),
                            Label("Username", style="font-weight: bold;color: black;"),
                            Input(type="text", name="username", placeholder="Choose a username", required=True),
                            Label("Email", style="font-weight: bold;color: black;"),
                            Input(type="email", name="email", placeholder="Enter your email", required=True),
                            Label("Password", style="font-weight: bold;color: black;"),
                            Input(type="password", name="password", placeholder="Choose a password", required=True),
                            Label("Confirm Password", style="font-weight: bold;color: black;"),
                            Input(type="password", name="confirm_password", placeholder="Confirm your password", required=True),

                            # ✅ FIXED: Ensure this button correctly posts to /signups
                            Button("Sign Up", type="submit", cls="button",
                                hx_post="/signups", hx_target="#signup-status",
                                style="width: 100%; background-color: #de4040; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;"),

                            A("Already have an account? Login here", href="/login", style="display: block; text-align: center; margin-top: 10px; color: #007bff; text-decoration: none;"),
                            Div(id="signup-status", style="margin-top: 10px; color: red; text-align: center;"),  # ✅ Feedback area
                            style="padding: 20px; background-color: #ffffff;",  
                        ),
                        id="signup-form",
                        style="max-width: 600px; margin: auto; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px; background-color: #ffffff;",  
                    ),
                    style="background-color: #ffffff;",
                )
            )
        )


    # Route for handling signups
    @dataclass
    class SignupData:
        first_name: str
        last_name: str
        username: str
        email: str
        password: str
        confirm_password: str

    @rt("/signups")
    def post_signup(data: SignupData):
        print("Received signup request:", data)

        if data.password != data.confirm_password:
            return "Passwords do not match"

        result = handle_signup(data.username, data.password, data.email, data.first_name, data.last_name)
        return result

    # Route for handling logins
    @dataclass
    class LoginData:
        username: str
        password: str

    @rt("/logins", methods=["POST"])
    def post_login(data: LoginData):
        print("Received login request:", data)

        result = handle_signin(data.username, data.password)
        return result






