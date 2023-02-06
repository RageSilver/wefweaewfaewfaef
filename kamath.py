import streamlit as st
import requests
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
st.set_page_config(page_title='My Website', page_icon=':tada:', layout='wide')

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



#Path Settings
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / 'assets'
STYLES_DIR = THIS_DIR / 'style'
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
#LOTTIE FILES
def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieur1("https://assets4.lottiefiles.com/packages/lf20_6xfdtlzb.json")
lotte_coding1 = load_lottieur1("https://assets2.lottiefiles.com/packages/lf20_skuagcud.json")
lottie_coding2 = load_lottieur1("https://assets4.lottiefiles.com/packages/lf20_vvpxhboz.json")

#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
#Images
img_contact_form = Image.open("images\eman.jpg")
img_contact_form1 = Image.open("images\powliner.png.jpg")
img_contact_form2 = Image.open("images\jeff.png.png")
img_contact_form3 = Image.open("images\money.png")
#Sub Header
with st.container():
    st.subheader("Hi, I am Vihaan Kamath!:wave:")
    st.title("A YouTuber From Canada")
    st.write("I am working on a Python Code this is a test. I will make this website about my YouTube channel!")
    st.write("[My YouTube Channel >](https://www.youtube.com/channel/UCtNNl-4R1_n8rI78SB11Wbw?app=desktop)")

#What i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I post")
        st.write("##")
        st.write(
        """
        On my Youtube Channel I create videos on Hypixel Skyblock! 
        - I post tutorials 
        - I post cool interviews 
        - I post nice videos 
        - Funny Videos
        - Post Weekly
        - Adventures I do! 
        If this sounds nice you should really consider subscribing and watch my videos!
        """
    )
    st.write("[Youtube Channel Link >](https://www.youtube.com/channel/UCtNNl-4R1_n8rI78SB11Wbw?app=desktop)") 
with right_column:
    st_lottie(lottie_coding, height=350, key='coding')

#Projects
with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column  = st.columns((1,2))
with image_column:
    st.image((img_contact_form), width=300)
    st.image((img_contact_form1), width=300)
    st.image((img_contact_form2), width=300)
with text_column:
    st.subheader("Watch RageSilver's Videos!")
    st.write(
        """
        Guides to certain achievments in Skyblock
        Step by Step toturials on how to do it 
        what gear is required and much much more!
        Here are my videos!
        This tutorial will help you!
        """
    )
    st.markdown("[Enderman t4 Guide...](https://www.youtube.com/watch?v=c_jaogKOCBM)")
    st.markdown("[Powliner Interview...](https://www.youtube.com/watch?v=BNtt6sJRBOI&t=370s)")
    st.markdown("[Interviewing a Billionaire...](https://www.youtube.com/watch?v=Fr19_7ansmA)")

#Donation Page
with st.container():
    st.write("---")
    st.header(PRODUCT_NAME)
    st.subheader(PRODUCT_TAGLINE)
    left_col, right_col = st.columns(2)
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    load_css_file(CSS_FILE)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button"> Click Here to Donate!</a>',
    unsafe_allow_html=True,
    )
with right_col:
    st_lottie(lottie_coding2, height=350)


#FAQ
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1: When Did I start Playing?": "I started in March 2020",
    "Question 2: Which server do I play on?": "I play Hypixel Skyblock" ,
    "Question 3: What is the server IP?": "I play on mc.hypixel.net",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)
#Contact Form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

contact_form = """ 
<form action="https://formsubmit.co/craftingking13@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email"required>
    <textarea input name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()