import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_gallery_photos(city):
    url = f"https://api.unsplash.com/search/photos?query={city}+travel&client_id={UNSPLASH_KEY}&per_page=6"
    try:
        res = requests.get(url).json()
        return [img['urls']['regular'] for img in res['results']]
    except:
        return ["https://images.unsplash.com/photo-1488646953014-85cb44e25828"] * 6

def get_ai_itinerary(dest, depart, days, budget, style, interests, transport):
    prompt = f"""
    Act as a professional Travel & Logistics Architect. 
    Plan a {days}-day trip to {dest} starting from {depart} using {transport}.
    Budget: {budget}, Style: {style}, Interests: {', '.join(interests)}.

    LOGISTICS RULES:
    1. Calculate travel time for {transport} between {depart} and {dest}.
    2. If distance is large (>800km) and mode is 'Train/Bus', dedicate Day 1 (and Day 2 if needed) to Transit. 
    3. If mode is 'Flight', include airport transfers and check-in on Day 1.
    4. Local Roaming: Suggest specific local transport (Auto, Scooters, Metro) based on {dest}.
    5. Format: Start with a 'LOGISTICS SUMMARY' box, then use 'DAY X: [Title]' for daily plans. Use emojis.
    """
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return chat.choices[0].message.content