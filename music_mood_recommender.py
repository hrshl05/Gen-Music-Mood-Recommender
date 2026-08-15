import webbrowser
import time

def suggest_music():
    print("--- Welcome to the Gen-Music Mood Recommender ---")
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number for age.")
        return

    gender = input("Enter your gender (male/female): ").lower()
    if gender not in ["male", "female"]:
        # ERROR: The original code only accepts "male" or "female" as valid..
        print("Please enter 'male' or 'female'.")
        return

    print("\nChoose your current mood:")
    print("1. Happy")
    print("2. Sad")
    print("3. Angry")
    
    choice = input("\nEnter choice (1/2/3): ")
    
    # Mapping choices to mood strings
    mood_map = {"1": "happy", "2": "sad", "3": "angry"}
    mood = mood_map.get(choice)

    if not mood:
        print("Invalid choice!")
        return

    # Music Database (Gender -> Age -> Mood -> Spotify playlist search link)
    # These open Spotify search results for playlists matching mood + age group + gender.
    music_db = {
        "male": {
            "youth": { # Age < 25
                "happy": "https://open.spotify.com/playlist/3JLXisgBk0SIiWJ9TwIUGG?si=psPpjL8CTreUHwO76-vAww",
                "sad": "https://open.spotify.com/playlist/2ZAvl3Q8VHVQELhb837jvu?si=WAI_-IFCQNeE15HlY88wPw",
                "angry": "https://open.spotify.com/playlist/0H9abOk1v9LUzp7O6ckbjl?si=Wx80Txh9Q7WIkhWjpz9STQ"
            },
            "adult": { # Age 25 to 50
                "happy": "https://open.spotify.com/playlist/7CMWUpkKkjlNL3mieglLLp?si=rp2Gxtd3S2Kj8kZjhXP2sw",
                "sad": "https://open.spotify.com/playlist/4x4S02KeNPo4Uv7jAPvyxi?si=x0POjb1-SGGNnqQ4jmTbmQ",
                "angry": "https://open.spotify.com/playlist/38KjfUKgPTzJsBwgCqqnOJ?si=AgILvPrgTO-4aaINKHnPpA&pi=Lud64FqyQaKIo"
            },
            "senior": { # Age > 50
                "happy": "https://open.spotify.com/playlist/02Wsd74kExl1dD4yGJ7ex2?si=Bke07Ez1SSikYV1UfsFCcg",
                "sad": "https://open.spotify.com/playlist/4fCUR9S3co96HrYivozhC7?si=HUCyTr6ATzCvCz36VRXA_g",
                "angry": "https://open.spotify.com/playlist/1eRZlHb96lxJk9WtEA2DN3?si=uYpSVoe0T7Ck64aU1yqX7A"
            }
        },# Replace with female-specific playlist
        "female": {
            "youth": { # Age < 25
                "happy": "https://open.spotify.com/playlist/4UBcAoCXSbk5LoONMwsMLR?si=BZcQ6oscSY6R69iFsNATcg&pi=5FM9SfyXRyKGv",  
                "sad": "https://open.spotify.com/playlist/3cWzKTOSy56AsVT7F7YpL4?si=XGfJqVikQHO9YZjB-HuzMw&pi=q9-Wd80PQXmG4",
                "angry": "https://open.spotify.com/playlist/6crrThibYPte7GVM49OD9S?si=XQ0sTM8MR2i2_4RD53mxqw&pi=KvIfsBHORVmnw"
            },
            "adult": { # Age 25 to 50
                "happy": "https://open.spotify.com/playlist/6kjx6EztY3cpqFLYmXUBb1?si=hPObgVRjTPePGXxulFTt4g",
                "sad": "https://open.spotify.com/playlist/7t6LAT93iK9yHG24uckOyJ?si=YFVKxBeXQHOiGN4HVja7Fw",
                "angry": "https://open.spotify.com/playlist/5necA67xetHmbGxHyVVtiv?si=h5nGWp93QiCfoGwyNoZZIw&pi=HJesZbqbSSi-y"
            },
            "senior": { # Age > 50
                "happy": "https://open.spotify.com/playlist/0NFTLburHHSZvBoncrgkNb?si=aKrsZBd5QIq0sh9IS177fw&pi=awalInHbSoi5w",
                "sad": "https://open.spotify.com/playlist/2hC3o5wWcLiKZ5bN7ZqDyy?si=ZdVyAv-MQMCg8GcuTpWu2A&pi=RPsojOqbTD-Id",
                "angry": "https://open.spotify.com/playlist/0G6HsHpUnsa1jzk7t9wyX0?si=0-MUPfWiQZSq0yJXisNYTA"
            }
        }
    }

    # Determine Age Group
    if age < 25:
        group = "youth"
    elif 25 <= age <= 40:
        group = "adult"
    else:
        group = "senior"

    # Get the playlist search link
    playlist_link = music_db[gender][group][mood]

    print(f"\nDetecting vibes for a {age} year old {gender} feeling {mood}...")

    # Delay to open the playlist to give the loading effect..
    time.sleep(1.5)

    print("Opening a Spotify Playlist search for your mood, age group, and gender...")

    # Opens the browser automatically to the playlist search results
    webbrowser.open(playlist_link)

if __name__ == "__main__":
    suggest_music()




