import streamlit as st
import random

from waffenkammer import waffen, schaden

st.write("# AXE Battle")
name = st.text_input("Wie heißt dein Kämpfer?")
if name == "":
    st.info("Gebe erst deinen Namen an")
    st.stop()
st.write("Hallo", name)

if "spielerleben" not in st.session_state:
    st.session_state['spielerleben'] = 10
    st.session_state['computerleben'] = 10
    st.session_state['runde'] = 1
spielerleben = st.session_state['spielerleben']
computerleben = st.session_state['computerleben']
runde = st.session_state['runde']

if runde == 1:
    st.write("Kampf beginnt...")
else:
    st.write("Runde", runde)
angriffart = st.radio("Wähle einen Angriff:", waffen.keys(), captions=waffen.values())

kampf_begonnen = st.button("FIGHT!")
if not kampf_begonnen:
    st.stop()

spielerschaden = schaden(angriffart)

computerangriff = random.choice(list(waffen.keys()))
computerschaden = schaden(computerangriff)

spielerleben = spielerleben - computerschaden
computerleben = computerleben - spielerschaden

st.write("Computer greift mit", computerangriff, "an...")
st.write("Spielerangriff: ", spielerschaden, "   Computerangriff: ", computerschaden)
st.write("Spielerleben: ", spielerleben,"   Computerleben: ", computerleben)

if spielerschaden > computerschaden:
    st.success("Du hast diese Runde gewonnen")
elif spielerleben == computerleben:
    st.info("Runde unentschieden")
else:
    st.error("Du hast diese Runde verloren")

runde = runde + 1
st.session_state['runde'] = runde

if spielerleben > 0 and computerleben > 0:
     # es geht weiter

    # hier speichern wir das Leben von Spieler und Computer nach dieser Runde
    st.session_state['spielerleben'] = spielerleben
    st.session_state['computerleben'] = computerleben
    st.stop()
elif spielerleben <= 0:
    st.error("Du hast den Kampf verloren")
elif computerleben <= 0:
    st.balloons()
    st.success("Du hast den Kampf gewonnen")
else:
   st.warning("Ihr seid leider beide gestorben.")

st.button('NEUER KAMPF')
del st.session_state['spielerleben']
del st.session_state['computerleben']