import streamlit as st
import json
import os

st.set_page_config(
    page_title="Login",
    layout="wide"
)

st.markdown("""
<style>

[data-testid="stSidebar"]{
display:none;
}

[data-testid="collapsedControl"]{
display:none;
}

section[data-testid="stSidebarNav"]{
display:none;
}

.stApp{
background:white;
}

h1,p,label{
color:#111827 !important;
}

.stButton > button{
    background:#111827 !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
    height:52px;
    font-weight:600 !important;
}

.stButton > button p{
    color:white !important;
}

.stButton > button span{
    color:white !important;
}

.stButton > button:hover{
    background:#1F2937 !important;
    color:white !important;
}

.stButton > button:hover p{
    color:white !important;
}

.stButton > button:hover span{
    color:white !important;
}

.stButton > button:focus{
    color:white !important;
}

.stButton > button:active{
    color:white !important;
}

.stTextInput input{
border-radius:12px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
text-align:center;
font-size:52px;
font-weight:800;
color:#111827;
margin-top:20px;
">
🔐 Welcome Back
</h1>

<p style="
text-align:center;
font-size:20px;
color:#6B7280;
margin-bottom:40px;
">
Sign in to access the Enterprise Change Intelligence Platform
</p>
""", unsafe_allow_html=True)

left, center, right = st.columns([1.5,2,1.5])

with center:

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    st.write("")

    if st.button(
        "Login",
        use_container_width=True
    ):

        try:

            BASE_DIR = os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )

            users_file = os.path.join(
                BASE_DIR,
                "users.json"
            )

            with open(users_file, "r") as f:
                users = json.load(f)

            if (
                username in users and
                users[username] == password
            ):

                st.session_state.logged_in = True
                st.session_state.user = username

                st.switch_page(
                    "pages/Dashboard.py"
                )

            else:

                st.error(
                    "Invalid Credentials"
                )

        except Exception as e:

            st.error(str(e))

    st.write("")

    if st.button(
        "📝 Create New Account",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Register.py"
        )