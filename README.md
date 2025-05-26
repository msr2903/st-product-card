# Streamlit Product Card Component

<img src="/assets/streamlit-product-card.jpg">

[![PyPI version](https://badge.fury.io/py/streamlit-product-card.svg)](https://badge.fury.io/py/streamlit-product-card)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A flexible and customizable Streamlit component designed to display product-like information cards within your applications. This component offers a range of features for controlling layout, image display, responsive behavior, styling, and interactivity.

## Features

* **Flexible Content:** Display name, description (single string or list), price, image, and an optional button.
* **Advanced Image Control:** Customize image position, aspect ratio ("native", "1/1", "16/9", etc.), object fit, and width percentage in horizontal layouts.
* **Responsive Design:** Configure mobile behavior for horizontal cards (stack top/bottom, shrink, or none) below a 600px breakpoint.
* **Customization & Styling:** Enable animations, load custom fonts via URL, and apply detailed CSS overrides using the `styles` prop (expects kebab-case CSS properties).
* **Interactivity:** Handle click events on the button (if present) or the entire card (if no button) via an `on_button_click` callback.

## Installation

If this component is packaged and released on PyPI:
```bash
pip install streamlit-product-card
```

## Usage

First, import the component:
```python
from streamlit_product_card import product_card
import streamlit as st
```

### Simple Example

<img src="/assets/simple-example.jpg">

```python
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
```

### Advanced Example

<img src="/assets/advanced-example.jpg">

```python
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
```

## API Reference

The `product_card` function accepts the following parameters:

| Prop Name                     | Type                               | Default        | Description                                                                                                                               |
|-------------------------------|------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `product_name`                | `str`                              | (Required)     | The main title for the product card.                                                                                                      |
| `description`                 | `Optional[Union[str, List[str]]]` | `None`         | A single string or a list of strings for the product description. Each string in a list will be rendered on a new line.                      |
| `price`                       | `Optional[Union[str, float]]]`     | `None`         | The price of the product.                                                                                                                 |
| `product_image`               | `Optional[str]`                    | `None`         | URL of the product image.                                                                                                                 |
| `button_text`                 | `Optional[str]`                    | `None`         | Text for the button. If `None` or an empty string, no button is rendered.                                                                |
| `picture_position`            | `str`                              | `"top"`        | Position of the image. Options: `"top"`, `"bottom"`, `"left"`, `"right"`.                                                                    |
| `enable_animation`            | `bool`                             | `True`         | If `True`, enables hover and active scaling animations on the card.                                                                       |
| `font_url`                    | `Optional[str]`                    | `None`         | URL to a CSS file for custom fonts (e.g., from Google Fonts).                                                                             |
| `image_width_percent`         | `Optional[int]`                    | `30`           | Percentage (0-100) for image `flex-basis` when `picture_position` is `"left"` or `"right"`.                                               |
| `image_aspect_ratio`          | `str`                              | `"native"`     | Image aspect ratio. Options: `"native"`, or CSS aspect-ratio strings (e.g., `"1/1"`, `"16/9"`).                                           |
| `image_object_fit`            | `str`                              | `"cover"`      | CSS `object-fit` property for the image (e.g., `"cover"`, `"contain"`).                                                                      |
| `mobile_breakpoint_behavior`  | `str`                              | `"stack top"`  | Behavior for horizontal cards on viewports ≤ 600px. Options: `"stack top"`, `"stack bottom"`, `"shrink"`, `"none"`.                        |
| `on_button_click`             | `Optional[Callable[[], Any]]`      | `None`         | Python callback for click events. Triggered by button (if present) or card (if no button).                                                 |
| `styles`                      | `Optional[Dict[str, Dict[str, Any]]]` | `None`         | Dictionary for custom CSS. Slots: `"card"`, `"title"`, `"text"`, `"price"`, `"button"`, `"image"`. Keys must be kebab-case (e.g., `font-family`). |
| `key`                         | `Optional[str]`                    | `None`         | A unique key for the Streamlit component.                                                                                                 |

**Returns:**
* **`bool`**: `True` if the `on_button_click` callback was invoked in the current Streamlit run due to a new click event from this specific card instance; `False` otherwise.

## 🙏 Acknowledgements

Originally forked from [gamcoh/st-card](https://github.com/gamcoh/st-card). Many thanks for their foundational work.
