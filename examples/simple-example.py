import streamlit as st
from streamlit_product_card import product_card

st.subheader("Simple Product Card")
clicked_basic = product_card(
    product_name="Elegant Watch",
    description="A timeless piece for every occasion.",
    price="€299.99",
    product_image="https://unsplash.com/photos/xfNeB1stZ_0/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzQ4MTY5NDIzfA&force=true&w=640",
    key="basic_card",
    picture_position="right",
    image_aspect_ratio="16/9",
    image_object_fit="cover",
)

if clicked_basic:
    st.write("Basic card's callback was triggered in this run.")