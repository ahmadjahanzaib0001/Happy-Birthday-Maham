import streamlit as st
import time

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(
    page_title="Happy Birthday Maham 🎉",
    page_icon="🎂",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #ff3399;'>🎂 Happy Birthday, Maham! 🎂</h1>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Messages
# -------------------------------
messages = [
    "Hey Maham 🌸",
    "Before anything else... I really want to say sorry for being such a headache these days ",
    "I have no right to interfere or say anything to you... and I’ve felt really bad about it.",
    "So, I thought I’d make up for it with something small but sincere 💫",
    "🎉🎉🎉",
    "HAPPY BIRTHDAY, MAHAM! 🎂",
    "Wishing you smiles, peace, and all the calm energy you deserve today (Which I ruined... sorry:( ) 💐",
    "Thanks for being patient — and for being a genuinely wonderful friend (if I really am a friend for you) 💛",
    "From your annoying but sincerely grateful friend (again, if I am)",
    "💖 Hope this little surprise made you smile 💖"
]

# -------------------------------
# Start Button
# -------------------------------
if st.button("Start the Surprise 🎁"):
    for msg in messages:
        st.markdown(f"<p style='font-size:18px; text-align:center'>{msg}</p>", unsafe_allow_html=True)
        time.sleep(2)  # simulate the Tkinter delay
    st.balloons()  # celebration effect
    st.success("Have the best birthday ever, Maham! 🎂💫")

# -------------------------------
# Footer
# -------------------------------
st.markdown("<hr>")
st.markdown("<p style='text-align: center; color: #666;'>Made with 💖 by your annoying friend :)</p>", unsafe_allow_html=True)

