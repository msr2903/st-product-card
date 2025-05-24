# -*- coding: utf-8 -*-
import os
from typing import Any, Callable, Dict, List, Optional, Union

import streamlit.components.v1 as components

# DEVELOPMENT MODE
_RELEASE = True
_COMPONENT_NAME = "streamlit_product_card"

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend", "build")
    _component = components.declare_component(_COMPONENT_NAME, path=build_dir)
else:
    _component = components.declare_component(
        _COMPONENT_NAME, url="http://localhost:3000"
    )


def product_card(
    product_name: str,
    description: Optional[Union[str, List[str]]] = None,
    price: Optional[Union[str, float]] = None,
    product_image: Optional[str] = None,
    button_text: str = "Add to Cart",
    use_button: bool = False,
    picture_position: str = "top",      # "top" | "bottom" | "left" | "right"
    picture_paddings: bool = False,
    enable_animation: bool = True,
    on_button_click: Optional[Callable[[], Any]] = None,
    styles: Optional[Dict[str, Dict[str, Any]]] = None,
    key: Optional[str] = None,
) -> bool:
    """
    Renders a product card.

    Args
    ----
    product_name      Title of the product.
    description       Optional string or list of strings.
    price             Optional string or number.
    product_image     Optional URL to the image.
    button_text       Label for the button.
    use_button        If True, only the button is clickable; default False.
    picture_position  One of "top", "bottom", "left", "right".
    picture_paddings  If True, adds inner padding around the image.
    enable_animation  If True, card scales on hover/active; default True.
    on_button_click   Callback when clicked.
    styles            CSS-in-JS overrides by slot.
    key               Streamlit component key.
    """
    # normalize description
    if description is None:
        desc_list: List[str] = []
    else:
        desc_list = description if isinstance(description, list) else [description]
    # normalize price
    price_str = "" if price is None else str(price)

    # merge default + user styles
    default_slots = ["card", "title", "text", "price", "button", "image"]
    merged_styles = {slot: {} for slot in default_slots}
    if styles:
        for slot, user in styles.items():
            if slot in merged_styles and isinstance(user, dict):
                merged_styles[slot].update(user)

    # call into React
    result = _component(
        productName=product_name,
        description=desc_list,
        price=price_str,
        productImage=product_image,
        buttonText=button_text,
        useButton=use_button,
        picturePosition=picture_position,
        picturePaddings=picture_paddings,
        enableAnimation=enable_animation,
        styles=merged_styles,
        key=key,
        default={"buttonClicked": False},
    )
    clicked = bool(result.get("buttonClicked", False))
    if clicked and on_button_click:
        on_button_click()
    return clicked