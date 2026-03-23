# VoyageAI: Intelligent Logistics & Itinerary Engine 🌍

**VoyageAI** is a modern, AI-powered travel planning dashboard designed to simplify trip orchestration. Unlike traditional planners, VoyageAI acts as a **Logistics Architect**, calculating real-world travel times based on your starting location and preferred mode of transport.

---

## 🚀 Key Features
- **AI-Driven Itineraries:** Powered by **Llama 3.3 70B (via Groq)** for ultra-fast, human-like travel suggestions.
- **Logistics Intelligence:** Automatically accounts for travel time (Transit Days) if the distance between cities is large.
- **Visual Exploration:** Dynamic 6-photo collage gallery fetched via **Unsplash API**.
- **Secure Authentication:** User signup and login system with **SHA-256 password hashing**.
- **Permanent Storage:** Save and manage your past trips using a local **SQLite Database**.
- **Interactive Mapping:** One-click integration with **Google Maps** for route visualization.
- **Theme Adaptive UI:** Modern "Glassmorphism" design that works perfectly in both Light and Dark modes.

---

## 🛠️ Technology Stack
- **Frontend:** Streamlit (Python-based Web Framework)
- **AI Engine:** Llama 3.3 70B (Groq Cloud API)
- **Database:** SQLite3
- **Image Integration:** Unsplash API
- **Language:** Python 3.9+
- **Security:** Hashlib (Password Encryption)

---

## 📂 Project Structure
```text
voyage_ai/
├── app.py           # Main UI Dashboard & Navigation
├── auth.py          # Security & Authentication Logic
├── database.py      # SQLite Database Management
├── utils.py         # AI Logic & Image API Integration
├── .env             # API Keys (Excluded from Git)
├── .gitignore       # Files to ignore in Git
└── requirements.txt # Project Dependencies
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/VoyageAI.git
   cd VoyageAI
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys:**
   Create a `.env` file in the root directory and add your keys:
   ```text
   GROQ_API_KEY=your_groq_key_here
   UNSPLASH_ACCESS_KEY=your_unsplash_key_here
   ```

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Author
**Karishma Saxena**  
