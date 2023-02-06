from pathlib import Path

import streamlit as st
from PIL import Image

#Path Settings
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / 'assets'
STYLES_DIR = THIS_DIR / 'styles'
CSS_FILE = STYLES_DIR/ "main.css"


#General Settings
STRIPE_CHECKOUT = "https://buy.stripe.com/test_bIYcQe16qdl36MUbII"
CONTACT_EMAIL = "craftingking13@gmail.com"
PRODUCT_NAME = "Donation to RageSilver"
PRODUCT_TAGLINE = "Ready to becoming a RageSilver member?"
PRODUCT_DESCRIPTION = """
There are many benefits to donating to RageSilver:

- Fund his videos
- Get specials perks on Youtube and Twitch
- Free merch

**DONATE**
"""
#Page Config
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)


#Main Section
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button"> Click Here to Donate!</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "product.png.jpg")
    st.image(product_image)
