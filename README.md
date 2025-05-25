# Streamlit Product Card Component

A flexible and customizable Streamlit component designed to display product-like information cards within your applications. This component offers a range of features for controlling layout, image display, responsive behavior, styling, and interactivity.

## Features

* **Core Content Display:**
    * `product_name`: The main title for the card.
    * `description`: Supports a single string or a list of strings for multi-line descriptions.
    * `price`: Displays the price of the item.
    * `product_image`: URL for the product's image.
* **Interactive Button:**
    * `button_text`: Text to display on the button. If `None` or an empty string is provided, no button will be rendered.
    * `on_button_click`: A Python callback function triggered when the button is clicked (if present) or when the card is clicked (if no button is present).
* **Image Control:**
    * `picture_position`: Control image placement ("top", "bottom", "left", or "right"). Default: `"top"`.
    * `image_width_percent`: Sets the image container's `flex-basis` (as a percentage of card width) when `picture_position` is "left" or "right". Default: `30`.
    * `image_aspect_ratio`: Define the aspect ratio for the image. Accepts "native" (to use the image's intrinsic ratio) or CSS aspect-ratio strings (e.g., "1/1" for square, "16/9", "4/3"). Default: `"native"`.
    * `image_object_fit`: Standard CSS `object-fit` property for the image (e.g., "cover", "contain", "fill"). Default: `"cover"`.
* **Responsive Behavior:**
    * `mobile_breakpoint_behavior`: Determines how cards with `picture_position="left"` or `"right"` adapt on viewports ≤ 600px.
        * `"stack top"` (Default): Image stacks above the content.
        * `"stack bottom"`: Image stacks below the content.
        * `"shrink"`: Image container attempts to shrink (visual effect depends on content and specific CSS).
        * `"none"`: Layout remains horizontal.
* **Customization & Styling:**
    * `enable_animation`: Enables a subtle scale animation on hover and active states. Default: `True`.
    * `font_url`: Optional URL to import custom web fonts (e.g., from Google Fonts).
    * `styles`: A dictionary to provide custom CSS overrides for different parts of the card (`card`, `title`, `text`, `price`, `button`, `image`). **CSS property keys should be in kebab-case** (e.g., `font-family`, `background-color`).
* **Standard Streamlit Support:**
    * `key`: Unique key for the Streamlit component.

## Installation

If this component is packaged and released on PyPI:
```bash
pip install streamlit-product-card
```

If you are using it locally:
1.  Ensure you have a `frontend` subfolder containing the React code.
2.  Build the frontend:
    ```bash
    cd frontend
    npm install # or yarn install
    npm run build # or yarn build
    ```
3.  Make sure the `_RELEASE = True` flag is set in the `__init__.py` file of the component when you want to use the built frontend. For development, set `_RELEASE = False` and run the frontend development server (usually `npm start` or `yarn start`).

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
            "color": "#BF360C" # Example color
        },
        "button": {
            "background-color": "#2C3E50",
            "color": "white",
            "font-weight": "bold",
            "border-radius": "5px"
        },
        "image": {
            "background-color": "#e0e0e0" // Visible if image is 'contain' and not filling
        }
    },
    mobile_breakpoint_behavior="stack top",
    key="advanced_camera"
)

if clicked_advanced:
    st.write("Advanced card's callback was triggered in this run.")
```

## API Reference

`product_card(product_name, description=None, price=None, product_image=None, button_text=None, picture_position="top", enable_animation=True, font_url=None, image_width_percent=30, image_aspect_ratio="native", image_object_fit="cover", mobile_breakpoint_behavior="stack top", on_button_click=None, styles=None, key=None)`

* **`product_name: str`**: The main title for the product card.
* **`description: Optional[Union[str, List[str]]] = None`**: A single string or a list of strings for the product description. Each string in a list will be rendered on a new line.
* **`price: Optional[Union[str, float]]] = None`**: The price of the product.
* **`product_image: Optional[str] = None`**: URL of the product image.
* **`button_text: Optional[str] = None`**: Text for the button. If `None` or an empty string, no button is rendered.
* **`picture_position: str = "top"`**: Position of the image relative to the text content. Options: `"top"`, `"bottom"`, `"left"`, `"right"`.
* **`enable_animation: bool = True`**: If `True`, enables hover and active scaling animations on the card.
* **`font_url: Optional[str] = None`**: URL to a CSS file for custom fonts (e.g., from Google Fonts).
* **`image_width_percent: Optional[int] = 30`**: Percentage (0-100) of the card's width that the image container should occupy when `picture_position` is `"left"` or `"right"`. This sets the `flex-basis`.
* **`image_aspect_ratio: str = "native"`**: Defines the aspect ratio for the image.
    * `"native"`: Uses the image's intrinsic aspect ratio.
    * CSS aspect-ratio string (e.g., `"1/1"`, `"16/9"`, `"4/3"`): Forces the image container to this ratio.
* **`image_object_fit: str = "cover"`**: Standard CSS `object-fit` property for the image (e.g., `"cover"`, `"contain"`, `"fill"`, `"scale-down"`, `"none"`).
* **`mobile_breakpoint_behavior: str = "stack top"`**: How the card layout (for originally horizontal `picture_position`) changes on viewports ≤ 600px.
    * `"stack top"`: Image stacks on top of the content.
    * `"stack bottom"`: Image stacks below the content.
    * `"shrink"`: Image container attempts to reduce its `flex-basis` (visual effect may vary).
    * `"none"`: Layout remains horizontal.
* **`on_button_click: Optional[Callable[[], Any]] = None`**: A Python function to call when the card/button is clicked. If a button is rendered (due to `button_text` being provided), only the button click triggers this. If no button is rendered, the entire card click triggers this callback.
* **`styles: Optional[Dict[str, Dict[str, Any]]] = None`**: A dictionary for applying custom CSS styles to different parts ("slots") of the card.
    * Slots: `"card"`, `"title"`, `"text"`, `"price"`, `"button"`, `"image"`.
    * **Important**: CSS property keys within the style dictionaries must be in **kebab-case** (e.g., `{'title': {'font-family': 'Arial', 'font-size': '1.2em'}}`).
* **`key: Optional[str] = None`**: A unique key for the Streamlit component, important for maintaining state and handling events correctly when multiple cards are used.

**Returns:**
* **`bool`**: `True` if the `on_button_click` callback was invoked in the current Streamlit run due to a new click event from this specific card instance; `False` otherwise.

## 🙏 Acknowledgements

Originally forked from [gamcoh/st-card](https://github.com/gamcoh/st-card). Many thanks for their foundational work.