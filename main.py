import streamlit as st
from streamlit_option_menu import option_menu
import Registration, Inspection_result

st.set_page_config(page_title="RFI_CCC")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = None
        with st.sidebar:
            st.markdown("<h1 style='color: orange; font-weight: bold;'>CCC_RFI</h1>", unsafe_allow_html=True)
            app = option_menu(
                menu_title="",
                options=["Registration", "Inspection_result"],
                icons=["house-fill", "person-circle"],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        for app_dict in self.apps:
            if app == app_dict["title"]:
                app_dict["function"]()

# Create an instance of MultiApp
multi_app = MultiApp()

# Add apps to the MultiApp instance
multi_app.add_app("Registration", Registration.app)
multi_app.add_app("Inspection_result", Inspection_result.app)

# Run the MultiApp instance
multi_app.run()