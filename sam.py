from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Smarty web",page_icon=":tada:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',  unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/ss.jpg")
img_github = Image.open("images/aa.jpg")

 

with st.container():
    st.subheader('A Computer Engineer Students Blog')
    st.title('Hi Im Samantha')
    st.write('BSCPE 1B Student')
    
with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What to know?")
        st.write("##")
        st.write(
            """
            I am a Computer Engineering Student, BSCPE 1-B and Im making a project with a contect of my girlgroup Idol.
             
            """
        )
        st.write('If you want to know how to create a webpage just click below')
    
    st.write("[For more information >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("BLACKPINK")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("BLACKPINK")
    st.write(
        """
        There are 4 members in the group named Lisa Manoban, Jennie Kim, Rose, and Jisoo. 
        """     
        )
    st.markdown("[watch the video...](https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2FgQlMMD8auMs%3Fsi%3DDHwOsRvpODJ4KQoV%26fbclid%3DIwAR3wzXLkE3BKQPp672PDsRPYvgB8EWFRU6AunugmVYeovh07vNaCGupjxM0&h=AT2n9LxrVLHLsRTnlke2bMpjLiJMpRgjvbSXGslzcVqsGO5CqmJJMbqw4P8SK0miB4PDbrchQr486hDNGUEM7PPdM7pxzMvCuIPffdOiH_QVMqXzameFGkICNbBWE7Onh-o_QA)")

with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_github)

with text_column:
    st.subheader("Their Journey")
    st.write(
        """
         This girl group is very famous to the International Music Industry. They have went through a lot of Challenges.
        """     
        )
    st.markdown("[watch the video...](https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2Fy8lal1cBHmM%3Fsi%3DZ5OI4La2NC5J5FbW%26fbclid%3DIwAR3YbDai2iPOwG3QqKtrd06izxSLCD1G7Xzf7QRkWl7ZMLUm4JjoDPM7YUA&h=AT2809mbR_WYcTyoxFrPRjaqRiitpncNvZ5wyo9WxSPCKqUNezHiailMQ-ht4CpQCk9LLbJhv7L6UJxQEcN7CN5GbogpBxkh7j6SWtq2ZQZWgVT707oErLolsMQ7RQVArAKO3Q)")

with st.container():
    st.write("---")
    st.header('For Any concerns You Can Contact Me!')
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/samanthaarmilla6@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message  here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
