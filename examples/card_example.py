import streamlit as st
from streamlit_product_card import product_card

st.set_page_config(layout="centered")
st.title("Product Card: Padding & Position & Animation Demo")
st.markdown("---")

positions = ["top", "bottom", "left", "right"]

for animate in (True, False):
    st.subheader(f"Animation {'On' if animate else 'Off'}")
    for pos in positions:
        st.markdown(f"**Position = {pos}, paddings=False**")
        if product_card(
            product_name=f"Anim={animate}, Pos={pos}, Pad=False",
            description="Demo description",
            price="¥1,000",
            product_image=(
                f"https://placehold.co/300x200/888888/000000?"
                f"text={pos.upper()}"
            ),
            use_button=False,
            picture_position=pos,
            picture_paddings=False,
            enable_animation=animate,
        ):
            st.success(
                f"{pos} clicked (no padding, anim={animate})"
            )

        st.markdown(f"**Position = {pos}, paddings=True**")
        if product_card(
            product_name=f"Anim={animate}, Pos={pos}, Pad=True",
            description="Demo description",
            price="¥1,000",
            product_image=(
                f"https://placehold.co/300x200/AAAAAA/000000?"
                f"text={pos.upper()}"
            ),
            use_button=False,
            picture_position=pos,
            picture_paddings=True,
            enable_animation=animate,
        ):
            st.success(
                f"{pos} clicked (padding, anim={animate})"
            )