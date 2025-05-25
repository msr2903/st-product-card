# Streamlit Product Card Component

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

### Basic Example

```python
import streamlit as st
from streamlit_product_card import product_card

st.subheader("Simple Product Card")
clicked_basic = product_card(
    product_name="Elegant Watch",
    description="A timeless piece for every occasion.",
    price="€299.99",
    product_image="[https://placehold.co/600x400/7B8FA1/FFFFFF?text=Watch](https://placehold.co/600x400/7B8FA1/FFFFFF?text=Watch)",
    button_text="View Details",
    on_button_click=lambda: st.toast("View Details clicked!"),
    key="basic_card"
)

if clicked_basic:
    st.write("Basic card's callback was triggered in this run.")
```

### Advanced Example

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
    product_image="[https://placehold.co/800x600/C9A77C/2C3E50?text=Vintage+Camera](https://placehold.co/800x600/C9A77C/2C3E50?text=Vintage+Camera)",
    button_text="Add to Collection",
    on_button_click=handle_advanced_click,
    picture_position="left",
    image_width_percent=40,
    image_aspect_ratio="4/3",
    image_object_fit="contain",
    enable_animation=True,
    font_url="[https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap](https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap)",
    styles={
        "card": {
            "background-color": "#f5f5f5",
            "border-radius": "10px",
            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)"
        },
        "title": {
            "font-family": "'Playfair Display', serif",
            "font-size": "1.5em",
            "color": "#333"
        },
        "text": {
            "font-family": "'Roboto', sans-serif",
            "font-size": "0.9em",
            "color": "#555"
        },
        "price": {
            "font-family": "'Roboto', sans-serif",
            "font-size": "1.2em",
            "font-weight": "bold",
            "color": "#BF360C"
        },
        "button": {
            "background-color": "#2C3E50",
            "color": "white",
            "font-weight": "bold",
            "border-radius": "5px"
        },
        "image": {
            "background-color": "#e0e0e0" 
        }
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