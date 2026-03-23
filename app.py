import streamlit as st
import database as db
import auth
import utils

# Final Project Name: VoyageAI
st.set_page_config(page_title="VoyageAI", layout="wide", page_icon="🌍")
db.init_db()

# Custom CSS for Modern UI and Theme-Adaptive Text
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    
    /* Login Page Styling */
    .login-container {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=2074&auto=format&fit=crop');
        background-size: cover; padding: 60px; border-radius: 20px; text-align: center; color: white;
    }

    /* Professional Gallery Grid */
    .collage-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: -15px; margin-bottom: 20px; }
    .collage-container img { width: 100%; height: 220px; object-fit: cover; border-radius: 10px; }

    /* Itinerary Cards */
    .itinerary-card {
        background: rgba(128, 128, 128, 0.08); padding: 25px; border-radius: 15px; 
        border-left: 10px solid #2563eb; margin-bottom: 20px; border: 1px solid rgba(128, 128, 128, 0.1);
    }
    .day-header { color: #2563eb; font-weight: 700; font-size: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# Session State Persistence
if 'plan' not in st.session_state: st.session_state.plan = None
if 'photos' not in st.session_state: st.session_state.photos = []

# --- LOGIN SCREEN ---
if 'user' not in st.session_state:
    cols = st.columns([1, 2, 1])
    with cols[1]:
        # 1. ADDED LOGIN GIF (Flying Plane)
        st.markdown('<div class="login-container"><h1>🌍 VoyageAI Pro</h1><p>Intelligent Logistics & Itinerary Engine</p></div>', unsafe_allow_html=True)
        choice = st.radio("Access Portal", ["Login", "Sign Up"], horizontal=True)
        email = st.text_input("Email")
        pwd = st.text_input("Password", type="password")
        if choice == "Login":
            if st.button("Sign In 🚀", use_container_width=True):
                if auth.login_user(email, pwd):
                    st.session_state.user = email
                    st.rerun()
                else:
                    st.error("Authentication Failed")
                    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bm5qZzR4eXJ3eHh4eXJ3eHh4eXJ3eHh4eXJ3eHh4JnVwPTE/u0b9k3K8YfW8w/giphy.gif", use_container_width=True)
        else:
            if st.button("Create Account ✨", use_container_width=True):
                if auth.signup_user(email, pwd): st.success("Account Created! You can now login.")
    st.stop()

# --- MAIN DASHBOARD ---
with st.sidebar:
    st.title("🗺️ Voyage Settings")
    st.write(f"User: **{st.session_state.user}**")
    if st.button("Logout"):
        del st.session_state.user
        st.rerun()
    st.divider()
    depart = st.text_input("🛫 From", "" , placeholder="Enter departure city")
    dest = st.text_input("📍 To", "" , placeholder="Enter destination city")
    transport = st.selectbox("🚆 Mode of Transport", ["Flight", "Train", "Bus", "Private Car"])
    days = st.slider("📅 Days", 1, 14, 5)
    budget = st.selectbox("💰 Budget", ["Economy", "Moderate", "Luxury"])
    style = st.selectbox("🎭 Travel Style", ["Relaxation", "Adventure", "Cultural", "Religious"])
    interests = st.multiselect("❤️ Interests", ["Nature", "Food", "History", "Nightlife", "Spirituality"])
    
    # 2. ADDED SIDEBAR GIF (Spinning Globe)
    st.divider()
    st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZDZpOG9ldXRuYzMyaWo5MzZnYXhsZDZsbjh5dTM0NXJjeXM0Y2lpaiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/8uanhJLIbG9G8MkpIP/giphy.gif", width=150)
    st.caption("Plan with VoyageAI")

    generate_btn = st.button("Generate Experience ✨", use_container_width=True)

# --- CONTENT DISPLAY ---
tab1, tab2 = st.tabs(["🗺️ Master Planner", "📜 My Saved Trips"])

with tab1:
    if generate_btn:
        if not depart or not dest:
            st.error("Please provide both cities!")
        else:
            # 3. ADDED CUSTOM GIF LOADER
            loading_placeholder = st.empty()
            with loading_placeholder.container():
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3NrczhkbjR5eHI4ZW16Mzd4eDdreDB6Y2ZtcTRiYnFpMzJmMHoxNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9GhVS2ZVaI1Yk/giphy.gif", width=300)
                st.write("### 🌍 AI is analyzing geography and fetching visuals...")
            
            # Perform Logic
            st.session_state.photos = utils.fetch_gallery_photos(dest)
            st.session_state.plan = utils.get_ai_itinerary(dest, depart, days, budget, style, interests, transport)
            st.session_state.last_dest, st.session_state.last_depart = dest, depart
            
            # Clear loader
            loading_placeholder.empty()

    # Display the Resulting Plan
    if st.session_state.plan:
        # 1. Responsive Gallery
        num_imgs = len(st.session_state.photos)
        cols = st.columns(3)
        for i in range(num_imgs):
            with cols[i % 3]: st.image(st.session_state.photos[i], width="stretch")
        
        # 2. Map Integration
        c1, c2 = st.columns([3, 1])
        with c1: st.title(f"{st.session_state.last_depart} ➔ {st.session_state.last_dest}")
        with c2:
            maps_url = f"https://www.google.com/maps/dir/{st.session_state.last_depart}/{st.session_state.last_dest}/"
            st.markdown(f'<a href="{maps_url}" target="_blank"><button style="width:100%; height:50px; background:#db4437; color:white; border:none; border-radius:10px; font-weight:bold; cursor:pointer;">📍 View Route Map</button></a>', unsafe_allow_html=True)
        
        # 3. Itinerary Rendering
        sections = st.session_state.plan.split("DAY ")
        if sections[0].strip():
            st.warning(f"🚍 **Logistics Summary:**\n\n{sections[0].strip()}")

        for s in sections[1:]:
            parts = s.split("\n", 1)
            if len(parts) > 1:
                title, body = parts[0], parts[1]
                st.markdown(f'<div class="itinerary-card"><div class="day-header">🗓️ DAY {title}</div><div>{body.replace("- ", "• ").replace("\n", "<br>")}</div></div>', unsafe_allow_html=True)
        
        if st.button("💾 Save Adventure to Database", use_container_width=True):
            db.save_trip(st.session_state.user, st.session_state.last_depart, st.session_state.last_dest, st.session_state.plan)
            st.toast("Adventure Archived! ✅")
    else:
        st.info("👋 Set your travel route in the sidebar to generate a logistics-aware itinerary.")

with tab2:
    st.header("Your Adventure History")
    trips = db.get_user_trips(st.session_state.user)
    if not trips: st.info("No trips saved yet.")
    for t_dest, t_content, t_date in trips:
        with st.expander(f"🚢 {t_dest} | {t_date[:10]}"):
            st.markdown(t_content)
