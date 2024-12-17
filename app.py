import streamlit as st

# Titel der App
st.title('Hallo, Streamlit!')

# Einfache Textausgabe
st.write('Dies ist eine einfache Streamlit-App.')

# Eingabefeld für den Benutzer
name = st.text_input('Wie heißt du?')

# Begrüßung basierend auf der Benutzereingabe
if name:
    st.write(f'Hallo, {name}!')

