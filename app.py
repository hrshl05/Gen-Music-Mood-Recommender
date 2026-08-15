import streamlit as st

st.set_page_config(
    page_title="Gen-Music Mood Recommender",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Gen-Music Mood Recommender")
st.write("Find a Spotify playlist based on your age, gender, and mood.")

st.divider()

# User Inputs
age = st.number_input(
    "🎂 Enter your age",
    min_value=1,
    max_value=100,
    value=21
)

gender = st.selectbox(
    "👤 Select your gender",
    ["Male", "Female"]
)

mood = st.selectbox(
    "🎭 Select your current mood",
    ["Happy", "Sad", "Angry"]
)

# Convert values
gender = gender.lower()
mood = mood.lower()

# Age Group
if age < 25:
    group = "youth"
elif age <= 40:
    group = "adult"
else:
    group = "senior"


# Music Database
music_db = {
    "male": {
        "youth": {
            "happy": "https://open.spotify.com/playlist/3JLXisgBk0SIiWJ9TwIUGG",
            "sad": "https://open.spotify.com/playlist/2ZAvl3Q8VHVQELhb837jvu",
            "angry": "https://open.spotify.com/playlist/0H9abOk1v9LUzp7O6ckbjl"
        },
        "adult": {
            "happy": "https://open.spotify.com/playlist/7CMWUpkKkjlNL3mieglLLp",
            "sad": "https://open.spotify.com/playlist/4x4S02KeNPo4Uv7jAPvyxi",
            "angry": "https://open.spotify.com/playlist/38KjfUKgPTzJsBwgCqqnOJ"
        },
        "senior": {
            "happy": "https://open.spotify.com/playlist/02Wsd74kExl1dD4yGJ7ex2",
            "sad": "https://open.spotify.com/playlist/4fCUR9S3co96HrYivozhC7",
            "angry": "https://open.spotify.com/playlist/1eRZlHb96lxJk9WtEA2DN3"
        }
    },

    "female": {
        "youth": {
            "happy": "https://open.spotify.com/playlist/4UBcAoCXSbk5LoONMwsMLR",
            "sad": "https://open.spotify.com/playlist/3cWzKTOSy56AsVT7F7YpL4",
            "angry": "https://open.spotify.com/playlist/6crrThibYPte7GVM49OD9S"
        },
        "adult": {
            "happy": "https://open.spotify.com/playlist/6kjx6EztY3cpqFLYmXUBb1",
            "sad": "https://open.spotify.com/playlist/7t6LAT93iK9yHG24uckOyJ",
            "angry": "https://open.spotify.com/playlist/5necA67xetHmbGxHyVVtiv"
        },
        "senior": {
            "happy": "https://open.spotify.com/playlist/0NFTLburHHSZvBoncrgkNb",
            "sad": "https://open.spotify.com/playlist/2hC3o5wWcLiKZ5bN7ZqDyy",
            "angry": "https://open.spotify.com/playlist/0G6HsHpUnsa1jzk7t9wyX0"
        }
    }
}


# Recommendation
playlist_link = music_db[gender][group][mood]

st.divider()

st.subheader("🎧 Your Recommendation")

st.success(
    f"Recommended playlist for a {int(age)} year old {gender} "
    f"in the {group} age group feeling {mood}."
)

st.link_button(
    "🎵 Open Recommended Spotify Playlist",
    playlist_link
)