# Streamlit Product Card

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
```

---

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
    product_image="https://placehold.co/300x200/007bff/white?text=Gadget+X",
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
    product_image="https://placehold.co/300x200/28a745/white?text=Another+Item",
    use_button=False,
    key="another_item_card"
)

if clicked_card:
    st.info("You clicked the 'Another Item' card!")
```

---

## 🔧 Parameters

| Parameter | Type | Default | Description |
|----------|------|---------|-------------|
| `product_name` | `str` | Required | Title of the product. |
| `description` | `str` or `List[str]` | `None` | Single string or list for multi-line descriptions. |
| `price` | `str` or `float` | `None` | Product price (converted to string). |
| `product_image` | `str` | `None` | URL of the product image. |
| `button_text` | `str` | `"Add to Cart"` | Text on the CTA button. |
| `use_button` | `bool` | `False` | If `True`, only the button is clickable. |
| `picture_position` | `str` | `"top"` | Image position: `"top"`, `"bottom"`, `"left"`, `"right"`. |
| `picture_paddings` | `bool` | `False` | Adds inner padding to the image. |
| `enable_animation` | `bool` | `True` | Enables card hover/active scaling. |
| `on_button_click` | `Callable[[], Any]` | `None` | Optional click callback function. |
| `styles` | `Dict[str, Dict[str, Any]]` | `None` | Custom CSS styles for card sections. |
| `key` | `str` | `None` | Unique key (required for multiple cards). |

---

## 🎨 Custom Styling

Customize the look using the `styles` parameter:

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
        "objectFit": "contain",
        "border": "2px solid #ddd"
    }
}
```

```python
product_card(
    product_name="Custom Style Product",
    description="This card demonstrates custom styling.",
    price="$49.99",
    product_image="https://placehold.co/300x200/ffc107/black?text=Styled",
    styles=custom_styles,
    key="custom_card"
)
```

---

## 🧪 Advanced Example

```python
import streamlit as st
from streamlit_product_card import product_card

st.set_page_config(layout="wide")
st.title("Product Card - Positions & Animations Demo")
st.markdown("---")

positions = ["top", "bottom", "left", "right"]

for animate in (True, False):
    st.subheader(f"Animation {'On' if animate else 'Off'}")
    cols = st.columns(len(positions))

    for i, pos in enumerate(positions):
        with cols[i]:
            st.markdown(f"**Pos: {pos}, Pad: False**")
            if product_card(
                product_name=f"Anim={animate}, Pos={pos}",
                description="Demo description",
                price="¥1,000",
                product_image=f"https://placehold.co/300x200/888888/000000?text={pos.upper()}",
                use_button=False,
                picture_position=pos,
                picture_paddings=False,
                enable_animation=animate,
                key=f"card_{animate}_{pos}_no_pad"
            ):
                st.success(f"{pos} clicked (no padding, anim={animate})")

            st.markdown(f"<br>**Pos: {pos}, Pad: True**", unsafe_allow_html=True)
            if product_card(
                product_name=f"Anim={animate}, Pos={pos}",
                description="Demo description",
                price="¥1,000",
                product_image=f"https://placehold.co/300x200/AAAAAA/000000?text={pos.upper()}",
                use_button=False,
                picture_position=pos,
                picture_paddings=True,
                enable_animation=animate,
                key=f"card_{animate}_{pos}_pad"
            ):
                st.success(f"{pos} clicked (padding, anim={animate})")

    st.markdown("---")
```

---

## 🛠️ Development

This component uses React for the frontend.

To modify the frontend:

```bash
cd your_package_name/frontend
npm install
npm start
```

To build for production:

```bash
npm run build
```

Be sure to update `_RELEASE` in `__init__.py`:
- `False` for development
- `True` for distribution

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

## 🙏 Acknowledgements

Originally forked from [gamcoh/st-card](https://github.com/gamcoh/st-card). Many thanks for their foundational work.