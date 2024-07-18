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
        app_titles = ["Select a Programme"] + [app_dict["title"] for app_dict in self.apps]
        
        # Initialize session state for selected_app if it doesn't exist
        if 'selected_app' not in st.session_state:
            st.session_state.selected_app = "Select a Programme"
        
        # Update session state based on the user's selection
        st.session_state.selected_app = st.sidebar.selectbox("Select a Programme:", app_titles, index=0)

        if st.session_state.selected_app == "Select a Programme":
            st.markdown(
                "<div style='display: flex; justify-content: center; align-items: center; height: 80vh;'><h2 style='color: red;'>Please select a programme from the dropdown list.</h2></div>",
                unsafe_allow_html=True,
            )
        else:
            for app_dict in self.apps:
                if st.session_state.selected_app == app_dict["title"]:
                    app_dict["function"]()

# Create an instance of MultiApp
multi_app = MultiApp()

# Add apps to the MultiApp instance
multi_app.add_app("Registration Programme", Registration.app)
multi_app.add_app("Inspection Result Programme", Inspection_result.app)

# Run the MultiApp instance
multi_app.run()
