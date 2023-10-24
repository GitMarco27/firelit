import os

import plotly.graph_objects as go
import streamlit as st
from PIL import Image

from firelit.frontend import firelit_login_form

if __name__ == "__main__":
    st.set_page_config(
        page_title="Firelit Demo App",
        page_icon="🔥",
        layout="wide",
    )

    with st.sidebar:
        image = Image.open(os.path.join("resources", "firelit_logo.png"))
        c1, c2, c3 = st.columns([1, 1, 1])
        c2.image(image, width=100)

    st.title("🔥 Firelit Demo App")
    st.subheader("This is a demo app for the Firelit package")
    sidebar = st.toggle("Show login form in the sidebar", key="sidebar_login")

    admin = firelit_login_form(sidebar=sidebar)

    if not admin.authentication_status:
        st.write("Please login to continue")
    else:
        fig = go.Figure(
            go.Barpolar(
                r=[3.5, 1.5, 2.5, 4.5, 4.5, 4, 3],
                theta=[65, 15, 210, 110, 312.5, 180, 270],
                width=[
                    20,
                    15,
                    10,
                    20,
                    15,
                    30,
                    15,
                ],
                marker_color=[
                    "#E4FF87",
                    "#709BFF",
                    "#709BFF",
                    "#FFAA70",
                    "#FFAA70",
                    "#FFDF70",
                    "#B6FFB4",
                ],
                marker_line_color="black",
                marker_line_width=2,
                opacity=0.8,
            )
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(range=[0, 5], showticklabels=False, ticks=""),
                angularaxis=dict(showticklabels=False, ticks=""),
            )
        )

        st.plotly_chart(fig, use_container_width=True)
