import streamlit as st
import random

from waffenkammer import waffen, schaden

st.write("# AXE Battle")
name = st.text_input("Wie heißt dein Kämpfer?")
if name == "":
    st.info("Gebe erst deinen Namen an")
    st.stop()
st.write("hallo", name)

if "spielerleben" not in st.session_state:
    st.session_state['spielerleben'] = 10
    st.session_state['computerleben'] = 10

st.write("Kampf beginnt...")
angriffart = st.radio("Wähle einen Angriff:", waffen.keys(), captions=waffen.values())

kampf_begonnen = st.button("FIGHT!")
if not kampf_begonnen:
    st.stop()

spielerschaden = schaden(angriffart)

computerangriff = random.choice(list(waffen.keys()))
computerschaden = schaden(computerangriff)

st.session_state['spielerleben'] = st.session_state['spielerleben'] - computerschaden
st.session_state['computerleben'] = st.session_state['computerleben'] - spielerschaden

st.write("Computer greift mit", computerangriff, "an...")
st.write("Spielerangriff: ", spielerschaden, "   Computerangriff: ", computerschaden)
st.write("Spielerleben: ", st.session_state['spielerleben'],"   Computerleben: ", st.session_state['computerleben'])
if st.session_state['spielerleben'] > st.session_state['computerleben']:
    st.success("Du hast gewonnen")
elif st.session_state['spielerleben'] == st.session_state['computerleben']:
    st.info("Unentschieden")
else:
    st.error("Du hast verloren")

