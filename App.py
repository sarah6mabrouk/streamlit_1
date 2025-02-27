"""import streamlit as st
st.title("this is a title")
st.write(" Welcome gomycoders")
st.header("Hello Programmers")
st.subheader("Deploy your App")

st.success("success")
st.info("information")
st.warning("warning")
st.error("error")

exp = ZeroDivisionError("trying to divide by 0")
st.exception(exp)
from PIL import Image
img = Image.open("cat.jpg")
st.image(img, width =200)

if st.checkbox("show/hide"):
    #display the text if the checkbox returns true value
    st.text("You're a cutie patootie")


status = st.radio("Slect Gender: ", {'Male', 'Female' ,'Dog'})

if (status == 'Male'):
    st.success("Male")
elif (status == 'Female'):
    st.success("Female")
else:
    st.warning("you're a dog")


hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("your hobby is ", hobby)

hobbies = st.multiselect('choose your hobbies: ', ['dancing', 'writing', 'reading'])
st.write('you selected', len(hobbies), 'hobbies')

if (st.button("about")):
    st.text("enter your name, type here...")
name = st.text_input("enter your name, 'type here...")

if (st.button("submit")):
    result = name.title()
    st.success(result)

level = st.slider("select the level", 1,5)
st.text("selected : {}".format(level))
"""

import streamlit as st
st.title("welcome to bmi calculator")
weight = st.number_input("enter your weight in kg")
status = st.radio("select your height format: ", ('cm', 'm', 'feet'))
if status == 'cms':
    height = st.number_input("centimers")
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text('enter some value of height')