import streamlit as st
from streamlit_product_card import product_card

st.subheader("Customized Product Card")

def handle_advanced_click():
    st.success("Advanced card's 'Add to Collection' button clicked!")

clicked_advanced = product_card(
    product_name="Vintage Camera",
    description=[
        "Capture moments with this classic vintage camera.",
        "Fully functional and restored by experts.",
        "Includes leather strap and original manual."
    ],
    price="€450",
    product_image="https://unsplash.com/photos/zagEcOkRFMk/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8MTl8fHZpbnRhZ2UlMjBjYW1lcmF8ZW58MHx8fHwxNzQ4MTU1MjI4fDA&force=true&w=640",
    on_button_click=handle_advanced_click,
    picture_position="right",
    image_width_percent=40,
    image_aspect_ratio="4/3",
    image_object_fit="cover",
    enable_animation=True,
    font_url="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
    styles={
        "card": {
            "border-radius": "12px",
            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
            "background-color": "#F4E0C2",
        },
        "title": {
            "font-family": "'Bodoni', serif",
            "font-size": "2.5em",
            "font-weight": "bold",
            "color": "#141413"
        },
        "text": {
            "font-family": "'Montserrat', sans-serif",
            "font-size": "0.9em",
            "color": "#141413"
        },
        "price": {
            "font-family": "'Montserrat', sans-serif",
            "font-size": "1.2em",
            "font-weight": "bold",
            "color": "#141413"
        },
    },
    mobile_breakpoint_behavior="stack top",
    key="advanced_camera"
)

if clicked_advanced:
    st.write("Advanced card's callback was triggered in this run.")