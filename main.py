import streamlit as st

# Ensure this is the first Streamlit command
st.set_page_config(page_title="RFI_CCC")

import Registration
import Inspection_result

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.markdown("<h1 style='color: orange; font-weight: bold;'>CCC_RFI</h1>", unsafe_allow_html=True)
        app_titles = ["Select a page"] + [app_dict["title"] for app_dict in self.apps]
        app_choice = st.sidebar.selectbox("Select a page:", app_titles)

        if app_choice == "Select a page":
            st.markdown(
                "<div style='display: flex; justify-content: center; align-items: center; height: 80vh;'><h2 style='color: red;'>Please select a program from the dropdown list.</h2></div>",
                unsafe_allow_html=True,
            )
        else:
            for app_dict in self.apps:
                if app_choice == app_dict["title"]:
                    app_dict["function"]()

# Create an instance of MultiApp
multi_app = MultiApp()

# Add apps to the MultiApp instance
multi_app.add_app("Registration", Registration.app)
multi_app.add_app("Inspection_result", Inspection_result.app)

# Run the MultiApp instance
multi_app.run()
