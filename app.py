import streamlit as st

st.set_page_config(page_title="🏎️ F1 2025 Teams & Drivers", layout="centered")
st.title("🏁 Formula 1 - 2025 Teams and Drivers")

# Dictionary of 2025 F1 teams and their drivers
f1_teams_2025 = {
    "Red Bull Racing": ["Max Verstappen", "Yuki Tsunoda"],
    "Ferrari": ["Charles Leclerc", "Lewis Hamilton"],
    "Mercedes": ["George Russell", "Andrea Kimi Antonelli"],
    "McLaren": ["Lando Norris", "Oscar Piastri"],
    "Aston Martin": ["Fernando Alonso", "Lance Stroll"],
    "Alpine": ["Pierre Gasly", "Jack Doohan"],
    "Williams": ["Alex Albon", "Carlos Sainz"],
    "Haas": ["Esteban Ocon", "Oliver Bearman"],
    "Racing Bulls": ["Liam Lawson", "Isack Hadjar"],
    "Sauber": ["Nico Hulkenberg", "Gabriel Bortoleto"]
}

# Team selection
selected_team = st.selectbox("Select a Formula 1 Team", list(f1_teams_2025.keys()))

# Display team drivers
st.subheader(f"🚗 Drivers for {selected_team} in 2025")
drivers = f1_teams_2025[selected_team]
for driver in drivers:
    st.write(f"• {driver}")
