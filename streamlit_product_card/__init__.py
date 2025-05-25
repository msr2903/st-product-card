# -*- coding: utf-8 -*-
import os
from typing import Any, Callable, Dict, List, Optional, Union
import streamlit as st # Import streamlit
import streamlit.components.v1 as components

_RELEASE = True
_COMPONENT_NAME = "streamlit_product_card"

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend", "build")
    _component = components.declare_component(_COMPONENT_NAME, path=build_dir)
else:
    _component = components.declare_component(
        _COMPONENT_NAME, url="http://localhost:3000" # Adjust port
    )


def product_card(
    product_name: str,
    description: Optional[Union[str, List[str]]] = None,
    price: Optional[Union[str, float]] = None,
    product_image: Optional[str] = None,
    button_text: Optional[str] = None, 
    picture_position: str = "top",      
    enable_animation: bool = True,
    font_url: Optional[str] = None,
    image_width_percent: Optional[int] = 30, 
    image_aspect_ratio: str = "native", 
    image_object_fit: str = "cover",    
    mobile_breakpoint_behavior: str = "none", 
    on_button_click: Optional[Callable[[], Any]] = None,
    styles: Optional[Dict[str, Dict[str, Any]]] = None,
    key: Optional[str] = None,
) -> bool:
    """
    Renders a product card. (Docstring content remains similar, focusing on props)
    ...
    Returns:
        bool: True if the on_button_click callback was invoked in the current run 
              due to a new click event, False otherwise.
    """
    if description is None:
        desc_list: List[str] = []
    else:
        desc_list = description if isinstance(description, list) else [description]
    price_str = "" if price is None else str(price)
    
    current_button_text = button_text if button_text is not None else ""
    current_styles = styles if styles is not None else {}
    current_image_width_percent = 30 
    if image_width_percent is not None:
        current_image_width_percent = image_width_percent

    # Ensure a unique session state key if the component key is provided
    # If no key is provided by the user, this event handling might not be instance-specific
    # which could be problematic for multiple cards without keys.
    # Streamlit generally requires keys for input elements to maintain state.
    # For robust event handling per card, a unique `key` prop is highly recommended.
    session_event_key = None
    if key:
        session_event_key = f"__product_card_{key}_last_event_id"
    elif product_name: # Fallback to product_name if no key, less ideal
        session_event_key = f"__product_card_{product_name}_last_event_id"


    component_value = _component(
        productName=product_name,
        description=desc_list,
        price=price_str,
        productImage=product_image,
        buttonText=current_button_text,
        picturePosition=picture_position,
        enableAnimation=enable_animation,
        fontUrl=font_url,
        imageWidthPercent=current_image_width_percent,
        imageAspectRatio=image_aspect_ratio,
        imageObjectFit=image_object_fit,
        mobileBreakpointBehavior=mobile_breakpoint_behavior,
        styles=current_styles, 
        key=key, # Pass the key to the component for Streamlit to manage its instance
        default={"clickEventId": None}, # Default value for our event tracking
    )

    clicked_in_this_run = False
    new_event_id = component_value.get("clickEventId")

    if new_event_id is not None:
        if session_event_key: # Only process if we have a way to track instance state
            if st.session_state.get(session_event_key) != new_event_id:
                st.session_state[session_event_key] = new_event_id
                if on_button_click:
                    on_button_click()
                clicked_in_this_run = True
        elif on_button_click: # Fallback for no key, but fires on every event from any such card
            # This branch is less ideal as it doesn't distinguish card instances well without a key
            # Consider warning the user if key is None but on_button_click is used.
            on_button_click()
            clicked_in_this_run = True


    return clicked_in_this_run
