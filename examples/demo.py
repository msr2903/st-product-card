import streamlit as st
from streamlit_product_card import product_card 

# --- Page Configuration ---
st.set_page_config(
    page_title="Product Card Showcase",
    page_icon="🛍️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Placeholder Image URLs ---
IMG_LANDSCAPE = "https://placehold.co/600x400/D1E8E2/116466?text=Landscape+600x400"
IMG_PORTRAIT = "https://placehold.co/400x600/FFCB9A/D24136?text=Portrait+400x600"
IMG_SQUARE_PLACEHOLDER = "https://placehold.co/500x500/C9E4DE/2C3532?text=Square+500x500"
IMG_WIDE = "https://placehold.co/800x300/F2D096/8E5044?text=Wide+800x300"
IMG_ANIMATION = "https://placehold.co/400x400/FFDAB9/8B4513?text=Animation+Demo"
IMG_FONT_MOCHIY = "https://placehold.co/400x250/05402A/F0FFF0?text=Mochiy+Pop+P+One+Font+-+Work+Sans"
IMG_FONT_CLAUDE = "https://placehold.co/400x400/E8E7DD/3C3A2A?text=Space+Grotesk"
IMG_FONT_VINTAGE = "https://placehold.co/400x400/53372E/D7CDC6?text=Old+Standard+TT+Fonts+-+Roboto+Slab"
IMG_CUSTOM_STYLES = "https://placehold.co/450x300/D3D3D3/000000?text=Custom+Styles"
IMG_MOBILE_STACK_TOP = "https://placehold.co/400x250/A2D2FF/003049?text=Stack+Top"
IMG_MOBILE_STACK_BOTTOM = "https://placehold.co/400x250/FBC4AB/D45769?text=Stack+Bottom" 
IMG_MOBILE_SHRINK = "https://placehold.co/300x300/FFB5A7/6D2E46?text=Shrink+Demo"
IMG_MOBILE_NONE = "https://placehold.co/350x200/BDE0FE/0077B6?text=No+Change"
IMG_CLICK_DEMO = "https://placehold.co/300x200/C1E1C1/2E8B57?text=Click+Me"
IMG_MINIMAL_DEMO = "https://placehold.co/300x150/EEEEEE/333?text=Minimal"

# --- Demo Page Functions ---

def show_intro():
    st.markdown(
        """
        Welcome to the interactive showcase for the `streamlit-product-card` component!

        This component allows for flexible display of product-like information.
        Explore the demos to see various configurations.

        👈 **Select a demo from the sidebar.**
        """
    )
    st.info("Styles in Python use kebab-case for CSS properties (e.g., `font-family`).")

def demo_core_content_fields():
    st.header("📦 Core Content Fields")
    st.markdown("This section shows how the card appears when optional fields are omitted.")

    st.subheader("1. Only Product Name (All Optional Fields Empty/None)")
    product_card(
        product_name="Product Name Only",
        description=None, 
        price=None,       
        product_image=None, 
        button_text=None,   
        key="core_name_only"
    )

    st.subheader("2. Name and Price")
    product_card(
        product_name="Stylish Gadget",
        price="€99.99",
        key="core_name_price"
    )

    st.subheader("3. Name and Description (List)")
    product_card(
        product_name="Book Title",
        description=["Chapter 1: The Beginning", "Chapter 2: The Middle", "Chapter 3: The End"],
        key="core_name_desc_list"
    )
    
    st.subheader("4. Name and Image")
    product_card(
        product_name="Art Print",
        product_image=IMG_MINIMAL_DEMO,
        image_aspect_ratio="1/1", 
        key="core_name_image"
    )

    st.subheader("5. Name, Price, and Button (No Image, No Description)")
    product_card(
        product_name="Service Subscription",
        price="€19/month",
        button_text="Subscribe Now",
        key="core_name_price_button"
    )
    
    st.subheader("6. All Core Fields Filled")
    product_card(
        product_name="Complete Product Example",
        description="A full description of this amazing item, highlighting its key features and benefits to the customer.",
        price="€129.00",
        product_image=IMG_LANDSCAPE,
        button_text="Add to Basket",
        key="core_all_filled"
    )

def demo_picture_position():
    st.header("📐 Picture Position (`picture_position`)")
    st.markdown("Demonstrates the four possible positions for the product image.")
    positions_ver = ["top", "bottom"]
    cols_ver = st.columns(len(positions_ver))

    for i, pos in enumerate(positions_ver):
        with cols_ver[i]:
            st.markdown(f"**{pos.capitalize()}**")
            product_card(
                product_name=f"Image {pos.capitalize()}",
                description="A short description.",
                price="€25",
                product_image=f"https://placehold.co/300x200/FEA889/4A403A?text=Pos: {pos.upper()}",
                picture_position=pos,
                styles={"card": {"min-height": "300px"} if pos in ["left", "right"] else {}},
                image_aspect_ratio="3/2",
                key=f"pic_pos_{pos}"
            )

    positions_hor = ["left", "right"]
    cols_hor = st.columns(len(positions_hor))
    for i, pos in enumerate(positions_hor):
        with cols_hor[i]:
            st.markdown(f"**{pos.capitalize()}**")
            product_card(
                product_name=f"Image {pos.capitalize()}",
                description="A short description.",
                price="€25",
                product_image=f"https://placehold.co/300x200/FEA889/4A403A?text=Pos: {pos.upper()}",
                picture_position=pos,
                styles={"card": {"min-height": "300px"} if pos in ["left", "right"] else {}},
                image_aspect_ratio="3/2",
                key=f"pic_pos_{pos}_hor" # Ensure unique key
            )


def demo_image_display_settings():
    st.header("🖼️ Image Display Settings (`image_aspect_ratio` & `image_object_fit`)")
    st.markdown(
        """
    - **`image_aspect_ratio`**: "native", "1/1" (for square), "16/9", etc.
    - **`image_object_fit`**: "cover" (default), "contain", "fill", "scale-down".
    """
    )

    st.subheader("1. Native Aspect Ratio")
    cols_native = st.columns(2)
    with cols_native[0]:
        product_card(product_name="Portrait (Native, Contain)", description=["`image_aspect_ratio='native'`", "`image_object_fit='contain'`"], product_image=IMG_PORTRAIT, picture_position="top", image_aspect_ratio="native", image_object_fit="contain", styles={"card": {"height": "450px"}, "image": {"background-color": "#f0f0f0"}}, key="img_display_native_portrait_contain")
    with cols_native[1]:
        product_card(product_name="Landscape (Native, Cover)", description=["`image_aspect_ratio='native'`", "`image_object_fit='cover'`"], product_image=IMG_LANDSCAPE, picture_position="top", image_aspect_ratio="native", image_object_fit="cover", styles={"card": {"height": "300px"}}, key="img_display_native_landscape_cover")
    
    st.divider()
    st.subheader("2. Forced Aspect Ratios (e.g., '1/1' for Square, '16/9')")
    cols_forced = st.columns(2)
    with cols_forced[0]:
        st.markdown("#### Square (Using '1/1')")
        product_card(product_name="Portrait to Square (Cover)", description=["`image_aspect_ratio='1/1'`", "`image_object_fit='cover'`"], product_image=IMG_PORTRAIT, picture_position="top", image_aspect_ratio="1/1", image_object_fit="cover", key="img_display_square_1_1_portrait_cover")
        product_card(product_name="Landscape to Square (Contain)", description=["`image_aspect_ratio='1/1'`", "`image_object_fit='contain'`"], product_image=IMG_LANDSCAPE, picture_position="top", image_aspect_ratio="1/1", image_object_fit="contain", styles={"image": {"background-color": "#e0e0e0"}}, key="img_display_square_1_1_landscape_contain")
    with cols_forced[1]:
        st.markdown("#### 16/9 Ratio")
        product_card(product_name="Wide Image in 16/9 (Cover)", description=["`image_aspect_ratio='16/9'`", "`image_object_fit='cover'`"], product_image=IMG_WIDE, picture_position="top", image_aspect_ratio="16/9", image_object_fit="cover", key="img_display_16_9_wide_cover")
        product_card(product_name="Square Image in 16/9 (Contain)", description=["`image_aspect_ratio='16/9'`", "`image_object_fit='contain'`"], product_image=IMG_SQUARE_PLACEHOLDER, picture_position="top", image_aspect_ratio="16/9", image_object_fit="contain", styles={"image": {"background-color": "#d0d0d0"}}, key="img_display_16_9_square_contain")
    
    st.divider()
    st.subheader("3. Object Fit Variations")
    st.write("Demonstrating different `image_object_fit` values with `image_aspect_ratio='1/1'`.")
    cols_fit = st.columns(4)
    fits = ["cover", "contain", "fill", "scale-down"]
    colors = ["FFADAD", "FFD6A5", "FDFFB6", "CAFFBF"]
    for i, fit_type in enumerate(fits):
        with cols_fit[i]:
            product_card(product_name=f"Fit: {fit_type.capitalize()}", description=[f"`image_aspect_ratio='1/1'`", f"`image_object_fit='{fit_type}'`"], product_image=f"https://placehold.co/600x300/{colors[i]}/333?text=600x300", picture_position="top", image_aspect_ratio="1/1", image_object_fit=fit_type, styles={"image": {"background-color": "#f9f9f9"}}, key=f"img_display_fit_type_{fit_type}")

def demo_image_width_percent():
    st.header("↔️ Image Width Percent (`image_width_percent`)")
    st.markdown("This prop controls the `flex-basis` of the image container when `picture_position` is 'left' or 'right'. Default is 30%.")
    
    st.subheader("1. Various Percentages (Image Left)")
    percentages = [15, 30, 50, 75]
    # Displaying these vertically for better readability in centered layout
    for i, percent in enumerate(percentages):
        st.markdown(f"**Image Left: {percent}%**")
        product_card(
            product_name=f"Img: {percent}%",
            description="Text fills remaining space. Card has a min-height for this demo.",
            price=f"€{percent * 2}",
            product_image=f"https://placehold.co/400x300/B2EBF2/00796B?text={percent}%25",
            picture_position="left",
            image_width_percent=percent,
            image_aspect_ratio="4/3", 
            styles={"card": {"min-height": "200px", "margin-bottom": "20px"}}, # Added margin
            key=f"img_width_left_{percent}"
        )
            
    st.subheader("2. Various Percentages (Image Right)")
    for i, percent in enumerate(percentages):
        st.markdown(f"**Image Right: {percent}%**")
        product_card(
            product_name=f"Img: {percent}%",
            description="Text fills remaining space. Card has a min-height for this demo.",
            price=f"€{percent * 2.5}",
            product_image=f"https://placehold.co/400x300/FFCCBC/BF360C?text={percent}%25",
            picture_position="right",
            image_width_percent=percent,
            image_aspect_ratio="4/3",
            styles={"card": {"min-height": "200px", "margin-bottom": "20px"}}, # Added margin
            key=f"img_width_right_{percent}"
        )

def demo_custom_fonts():
    st.header("🔤 Custom Fonts (`font_url`)")
    st.markdown("Demonstrates loading and applying custom fonts using the `font_url` prop and `styles` for specific elements.")

    st.subheader("Example 1: Mochiy Pop P One & Work Sans")
    product_card(
        product_name="Kawaii Matcha Delight", # Changed product name
        description=[
            "A super cute and energizing matcha latte, crafted with premium Uji matcha.",
            "Topped with adorable latte art for an extra smile!"
        ],
        price="¥850", # Changed price
        product_image=IMG_FONT_MOCHIY, # Using a dedicated image
        picture_position="top", # Changed for better focus on text
        image_aspect_ratio="400/250", # Adjusted to image
        font_url="https://fonts.googleapis.com/css2?family=Mochiy+Pop+P+One&family=Work+Sans:wght@300;400;600;700&display=swap",
        styles={
            "card": {"font-family": "'Work Sans', sans-serif","background-color": "#F0FFF0"},
            "title": {
                "font-family": "'Mochiy Pop P One', sans-serif", 
                "font-size": "2.0em",
                "color": "#2E8B57",
                "margin-bottom": "10px"
            },
            "text": {
                "font-family": "'Work Sans', sans-serif",
                "font-size": "1.0em", # Example font size
                "color": "#4A4A4A",    # Darker gray for text
                "line-height": "1.6"
            },
            "price": {
                "font-family": "'Work Sans', sans-serif",
                "font-size": "1.3em",   # Example font size
                "font-weight": "600",   # Semi-bold
                "color": "#3CB371",     # MediumSeaGreen
                "margin-top": "10px"
            },
            "button": {
                "font-family": "'Work Sans', sans-serif", 
                "font-weight": "600",
                "background-color": "#3CB371",
                "color": "white",
                "font-size": "0.9em"
            }
        },
        button_text="Order Now!",
        key="font_example_mochiy_work_sans"
    )


    st.subheader("Example 2: Claude Style Product Button (Space Grotesk)")
    product_card(
        product_name="Claude Style Product Button",
        description="You can pass any fonts from Google Fonts to make it look like what you want. This example uses Space Grotesk to make it looks like Claude Design.",
        price="€75.00",
        product_image=IMG_FONT_CLAUDE,
        picture_position="left",
        image_width_percent=35,
        image_aspect_ratio="1/1",
        font_url="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap",
        styles={
            "card": {"background-color": "#F4F3ED",},
            "title": {"font-family": "'Space Grotesk', sans-serif", "font-weight": "700", "letter-spacing": "1px", "font-size": "1.7em", "color": "#3C3A2A"},
            "text": {"font-family": "'Space Grotesk', sans-serif","font-size": "0.9em", "color": "#3C3A2A"},
            "price": {"font-family": "'Space Grotesk', sans-serif", "font-weight": "500", "font-size": "1.1em", "color": "#BB5A38"},
            "button": {"font-family": "'Space Grotesk', sans-serif", "font-weight": "500", "background-color": "#BB5A38"},
        },
        button_text="Details",
        key="font_example_2"
    )

    st.subheader("Example 3: Vintage Newspaper Style (Old Standard TT & Roboto Slab)")
    product_card(
        product_name="The Daily Chronicle",
        description="Extra! Extra! Read all about the latest happenings in the world of vintage product cards. Get your copy today!",
        price="€0.50",
        product_image=IMG_FONT_VINTAGE,
        picture_position="right",
        image_width_percent=25,
        image_aspect_ratio="1/1",
        image_object_fit="cover",
        font_url="https://fonts.googleapis.com/css2?family=Old+Standard+TT:wght@400;700&family=Roboto+Slab:wght@400&display=swap",
        styles={
            "card": {"background-color": "#D7CDC6",}, 
            "title": {"font-family": "'Old Standard TT', serif", "font-weight": "700", "font-size": "1.8em", "color": "#5d4037"},
            "text": {"font-family": "'Roboto Slab', serif", "line-height": "1.6", "font-size": "0.9em", "color": "#5d4037"},
            "price": {"font-family": "'Old Standard TT', serif", "font-weight": "400", "font-size": "1.1em", "color": "#5d4037"},
            "button": {"font-family": "'Roboto Slab', serif", "font-weight": "400", "font-size": "0.9em", "background-color": "#53372E",}
        },
        button_text="Read More",
        key="font_example_3"
    )


def demo_on_button_click():
    st.header("🖱️ Click Events (`on_button_click`)")
    st.markdown(
        """
        This demonstrates the `on_button_click` callback.
        - If a `button_text` is provided, only the button click triggers the callback.
        - If `button_text` is empty or `None`, the entire card click triggers the callback.
        """
    )

    if 'click_message' not in st.session_state:
        st.session_state.click_message = "No card clicked yet."

    def handle_card_click(card_name):
        st.session_state.click_message = f"'{card_name}' was clicked!"
        st.toast(f"Clicked: {card_name}")


    st.info(f"Last event: {st.session_state.click_message}")

    st.subheader("1. Card with a Button")
    product_card(
        product_name="Interactive Item",
        description="Click the button below.",
        price="€42.00",
        product_image=IMG_CLICK_DEMO,
        button_text="Click Me!",
        on_button_click=lambda: handle_card_click("Interactive Item Button"),
        key="click_demo_button"
    )

    st.subheader("2. Card without a Button (Entire Card Clickable)")
    product_card(
        product_name="Clickable Card Area",
        description="Click anywhere on this card.",
        price="€20.00",
        product_image=IMG_CLICK_DEMO,
        button_text="", 
        on_button_click=lambda: handle_card_click("Clickable Card Area"),
        key="click_demo_no_button"
    )
    
    st.subheader("3. Card with Button (No Callback Attached)")
    product_card(
        product_name="Button, No Action",
        description="This button exists but has no `on_button_click` callback.",
        price="€15.00",
        product_image=IMG_CLICK_DEMO,
        button_text="Button (No Op)",
        key="click_demo_button_no_op"
    )


def demo_styling_and_animation_streamlined():
    st.header("💅 Styling & Animation (Streamlined)")
    st.markdown("Showcasing: `enable_animation` and advanced `styles` prop (using kebab-case).")

    st.subheader("1. Hover & Active Animations")
    cols_anim = st.columns(2)
    with cols_anim[0]:
        st.markdown("**Animation Enabled**")
        product_card(product_name="Animated Card", description="Hover/click for effects.", product_image=IMG_ANIMATION, picture_position="top", image_aspect_ratio="1/1", enable_animation=True, key="s_anim_enabled")
    with cols_anim[1]:
        st.markdown("**Animation Disabled**")
        product_card(product_name="Static Card", description="No scaling effects.", product_image=IMG_ANIMATION, picture_position="top", image_aspect_ratio="1/1", enable_animation=False, key="s_anim_disabled")
    
    st.divider()
    st.subheader("2. Advanced Custom Styling with `styles` Prop")
    product_card(
        product_name="Heavily Styled Card", 
        description="Custom borders, shadows, colors, etc.", 
        price="SALE: €19.99", 
        product_image=IMG_CUSTOM_STYLES, 
        picture_position="top", 
        image_aspect_ratio="45/30", 
        image_object_fit="contain", 
        styles={
            "card": {
                "border": "2px solid #007bff", "border-radius": "20px",
                "box-shadow": "0 10px 30px rgba(0, 123, 255, 0.3)",
                "background-color": "#f0f8ff", "max-width": "400px", "margin": "0 auto"
            },
            "image": { 
                "border": "5px dotted #28a745", "padding": "10px", "box-sizing": "border-box",
                "border-radius": "15px", "background-color": "#e9f5e9"
            },
            "title": {"color": "#dc3545", "text-align": "center", "text-transform": "uppercase", "letter-spacing": "1.5px"},
            "text": {"color": "#6c757d", "font-style": "italic", "line-height": "1.8"},
            "price": {"color": "white", "background-color": "#17a2b8", "padding": "5px 10px", "border-radius": "5px", "text-align": "center", "font-weight": "bold"},
            "button": {"background-color": "#ffc107", "color": "black", "border": "2px solid #e0a800", "border-radius": "0px", "text-transform": "uppercase", "font-weight": "900", "width": "100%"}
        }, 
        button_text="Grab Deal!", 
        key="s_heavily_styled"
    )


def demo_mobile_behavior(): 
    st.header("📱 Mobile Breakpoint Behavior")
    st.markdown("`mobile_breakpoint_behavior` for horizontal cards (<=600px). **Resize browser to observe.**")
    
    st.subheader("1. Behavior: `stack top` (Default)")
    product_card(product_name="Stack Top (Left Img)", description="Original: Img Left. Mobile: Img Top.", product_image=IMG_MOBILE_STACK_TOP, picture_position="left", image_width_percent=40, image_aspect_ratio="40/25", mobile_breakpoint_behavior="stack top", key="mobile_stack_top_left_page4")
    product_card(product_name="Stack Top (Right Img)", description="Original: Img Right. Mobile: Img Top.", product_image=IMG_MOBILE_STACK_TOP, picture_position="right", image_width_percent=40, image_aspect_ratio="40/25", mobile_breakpoint_behavior="stack top", key="mobile_stack_top_right_page4")

    st.divider()
    st.subheader("2. Behavior: `stack bottom`")
    product_card(product_name="Stack Bottom (Left Img)", description="Original: Img Left. Mobile: Img Bottom.", product_image=IMG_MOBILE_STACK_BOTTOM, picture_position="left", image_width_percent=40, image_aspect_ratio="40/25", mobile_breakpoint_behavior="stack bottom", key="mobile_stack_bottom_left_page4")
    product_card(product_name="Stack Bottom (Right Img)", description="Original: Img Right. Mobile: Img Bottom.", product_image=IMG_MOBILE_STACK_BOTTOM, picture_position="right", image_width_percent=40, image_aspect_ratio="40/25", mobile_breakpoint_behavior="stack bottom", key="mobile_stack_bottom_right_page4")

    st.divider()
    st.subheader("3. Behavior: `shrink` (Conceptual)")
    st.warning("Visual effect of 'shrink' is subtle.")
    product_card(product_name="Shrink Concept (Left Img)", description="Attempts to shrink image on mobile.", product_image=IMG_MOBILE_SHRINK, picture_position="left", image_width_percent=50, image_aspect_ratio="1/1", mobile_breakpoint_behavior="shrink", key="mobile_shrink_left_page4")

    st.divider()
    st.subheader("4. Behavior: `none`")
    product_card(product_name="No Change (Left Img)", description="Layout stays horizontal.", product_image=IMG_MOBILE_NONE, picture_position="left", image_width_percent=35, image_aspect_ratio="35/20", mobile_breakpoint_behavior="none", key="mobile_none_left_page4")

# --- Main App Logic ---
st.title("🛍️ Modernised Product Card Showcase")

st.sidebar.title("Demo Sections")
demo_options = {
    "🏠 Welcome": show_intro,
    "📦 Core Content": demo_core_content_fields,
    "📐 Picture Position": demo_picture_position,
    "🖼️ Image Display": demo_image_display_settings,
    "↔️ Image Width %": demo_image_width_percent,
    "🔤 Custom Fonts": demo_custom_fonts,
    "🖱️ Click Events": demo_on_button_click,
    "💅 Styling & Animation": demo_styling_and_animation_streamlined,
    "📱 Mobile Behavior": demo_mobile_behavior,
}
selected_demo_name = st.sidebar.radio("Choose a demo:", list(demo_options.keys()))

demo_function = demo_options[selected_demo_name]
demo_function()

st.sidebar.markdown("---")
st.sidebar.info("Resize browser to see responsive behaviors.")

