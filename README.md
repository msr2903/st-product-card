# Streamlit Product Card

[![PyPI version](https://img.shields.io/pypi/v/streamlit-product-card.svg)](https://pypi.org/project/streamlit-product-card/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**An e-commerce style product card component for Streamlit applications.**

Easily display products with images, descriptions, prices, and an optional call-to-action button — all with customizable styling and layout.

> **Note:** This project is forked from [gamcoh/st-card](https://github.com/gamcoh/st-card) and has been adapted and extended.

---

## ✨ Features

- **Product Information**: Product name, multi-line description, and price.
- **Image Display**: Position image at the top, bottom, left, or right.
- **Call-to-Action**: Optional button with customizable text.
- **Click Handling**:
  - Make the entire card clickable.
  - Make only the button clickable.
  - Returns `True` when the designated element is clicked.
- **Customization**:
  - Image padding.
  - Enable/disable animations.
  - CSS-in-JS style overrides for different card sections.
- **Theme Aware**: Integrates with Streamlit theming.

---

## 📦 Installation

```bash
pip install streamlit-product-card
````

-----

## 🚀 Basic Usage

```python
import streamlit as st
from streamlit_product_card import product_card

st.set_page_config(layout="centered")
st.title("My Awesome Product")

clicked = product_card(
    product_name="Cool Gadget X",
    description=["High-quality materials", "Latest technology", "Eco-friendly"],
    price="$99.99",
    product_image="[https://placehold.co/300x200/007bff/white?text=Gadget+X](https://placehold.co/300x200/007bff/white?text=Gadget+X)",
    button_text="Buy Now",
    use_button=True,
    picture_position="top",
    enable_animation=True
)

if clicked:
    st.success("You clicked 'Buy Now' for Cool Gadget X!")
```

**Entire Card Clickable Example**:

```python
clicked_card = product_card(
    product_name="Another Item",
    description="A brief description of this other item.",
    product_image="[https://placehold.co/300x200/28a745/white?text=Another+Item](https://placehold.co/300x200/28a745/white?text=Another+Item)",
    use_button=False, # Entire card is clickable
    key="another_item_card" # Important for multiple components
)

if clicked_card:
    st.info("You clicked the 'Another Item' card!")
```

-----

## 🔧 Parameters

The `product_card` function accepts the following parameters:

| Parameter          | Type                            | Default         | Description                                                                          |
|--------------------|---------------------------------|-----------------|--------------------------------------------------------------------------------------|
| `product_name`     | `str`                           | **Required** | Title of the product.                                                                |
| `description`      | `str` or `List[str]`            | `None`          | Single string or list for multi-line descriptions.                                   |
| `price`            | `str` or `float`                | `None`          | Product price (will be converted to string).                                         |
| `product_image`    | `str`                           | `None`          | URL of the product image.                                                            |
| `button_text`      | `str`                           | `"Add to Cart"` | Text on the CTA button.                                                              |
| `use_button`       | `bool`                          | `False`         | If `True`, only the button is clickable. Otherwise, the whole card is.               |
| `picture_position` | `str`                           | `"top"`         | Image position: `"top"`, `"bottom"`, `"left"`, `"right"`.                            |
| `picture_paddings` | `bool`                          | `False`         | If `True`, adds inner padding to the image, matching card radius.                    |
| `enable_animation` | `bool`                          | `True`          | Enables card hover/active scaling animation.                                         |
| `on_button_click`  | `Optional[Callable[[], Any]]`   | `None`          | Optional callback function invoked when the card/button is clicked.                  |
| `styles`           | `Optional[Dict[str, Dict[str, Any]]]` | `None`    | Custom CSS-in-JS styles for card sections (see "Custom Styling" below).              |
| `key`              | `Optional[str]`                 | `None`          | Unique Streamlit key, essential if you have multiple `product_card` components.        |

**Returns:**

  * `(bool)`: `True` if the card (or button, if `use_button=True`) was clicked in the last interaction, `False` otherwise.

-----

## 🎨 Custom Styling

Customize the look using the `styles` parameter. It accepts a dictionary where keys are "slots" (parts of the card) and values are dictionaries of CSS properties (use camelCase for CSS properties, e.g., `backgroundColor`).

Available slots for styling:

  * `card`: The main card container.
  * `title`: The product name.
  * `text`: The description area.
  * `price`: The price tag.
  * `button`: The button.
  * `image`: The product image.

**Example:**

```python
custom_styles = {
    "card": {
        "backgroundColor": "#f0f2f6",
        "borderRadius": "15px",
        "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
    },
    "title": {
        "color": "#1a73e8",
        "fontSize": "1.5rem",
        "fontWeight": "bold"
    },
    "text": {
        "fontStyle": "italic"
    },
    "price": {
        "color": "green",
        "fontSize": "1.8rem"
    },
    "button": {
        "backgroundColor": "#ff4b4b",
        "color": "white",
        "borderRadius": "20px",
        "padding": "12px 24px"
    },
    "image": {
        "objectFit": "contain", # Options: 'cover', 'contain', 'fill', 'scale-down'
        "border": "2px solid #ddd"
    }
}

product_card(
    product_name="Custom Style Product",
    description="This card demonstrates custom styling.",
    price="$49.99",
    product_image="[https://placehold.co/300x200/ffc107/black?text=Styled](https://placehold.co/300x200/ffc107/black?text=Styled)",
    styles=custom_styles,
    key="custom_card"
)
```

-----

## 🧪 Advanced Example

This example demonstrates iterating through different image positions and animation states.

```python
import streamlit as st
from streamlit_product_card import product_card

st.set_page_config(layout="wide")
st.title("Product Card - Positions & Animations Demo")
st.markdown("---")

positions = ["top", "bottom", "left", "right"]

for animate in (True, False):
    st.subheader(f"Animation {'On' if animate else 'Off'}")
    cols = st.columns(len(positions)) # Create columns for horizontal layout

    for i, pos in enumerate(positions):
        with cols[i]:
            st.markdown(f"**Pos: {pos}, Pad: False**")
            if product_card(
                product_name=f"Anim={animate}, Pos={pos}",
                description="Demo description",
                price="¥1,000",
                product_image=(
                    f"[https://placehold.co/300x200/888888/000000](https://placehold.co/300x200/888888/000000)?"
                    f"text={pos.upper()}"
                ),
                use_button=False,
                picture_position=pos,
                picture_paddings=False,
                enable_animation=animate,
                key=f"card_{animate}_{pos}_no_pad" # Unique key is important
            ):
                st.success(
                    f"{pos} clicked (no padding, anim={animate})"
                )

            st.markdown(f"<br>**Pos: {pos}, Pad: True**", unsafe_allow_html=True) # Add some space
            if product_card(
                product_name=f"Anim={animate}, Pos={pos}",
                description="Demo description",
                price="¥1,000",
                product_image=(
                    f"[https://placehold.co/300x200/AAAAAA/000000](https://placehold.co/300x200/AAAAAA/000000)?"
                    f"text={pos.upper()}"
                ),
                use_button=False,
                picture_position=pos,
                picture_paddings=True,
                enable_animation=animate,
                key=f"card_{animate}_{pos}_pad" # Unique key
            ):
                st.success(
                    f"{pos} clicked (padding, anim={animate})"
                )
    st.markdown("---") # Separator after each animation group
```

-----

## 🛠️ Development

This component is built with React for the frontend.

To modify the frontend:

1.  Navigate to the frontend directory:
    ```bash
    cd your_package_name/frontend 
    ```
    *(Remember to replace `your_package_name` with your actual package directory name, e.g., `streamlit_product_card`)*
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the development server:
    ```bash
    npm start
    ```

To build the frontend for production:

```bash
npm run build
```

Ensure you set `_RELEASE = False` in `your_package_name/__init__.py` for development and `_RELEASE = True` when packaging for distribution.

-----

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
*(Make sure you have a `LICENSE` file in the root of your project that this link can point to.)*

-----

## 🤝 Contributing

Contributions are welcome\! Please feel free to submit a pull request or open an issue.

-----

## 🙏 Acknowledgements

Originally forked from [gamcoh/st-card](https://github.com/gamcoh/st-card). Many thanks for their foundational work.