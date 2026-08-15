# 🎵 Gen-Music Mood Recommender

A Python-based music recommendation system that suggests Spotify playlists based on the user's **age, gender, and current mood**.

The program takes user preferences, determines the appropriate age group, and automatically opens a matching Spotify playlist in the web browser.

## ✨ Features

* 🎂 Age-based music recommendations
* 👤 Gender-based playlist selection
* 🎭 Mood-based recommendations
* 😊 Happy mood playlist
* 😔 Sad mood playlist
* 😡 Angry mood playlist
* 🎧 Spotify playlist integration
* 🌐 Automatically opens the recommended playlist in the browser
* 💻 Simple and beginner-friendly command-line interface

## 🛠️ Technologies Used

* **Python 3**
* `webbrowser` module
* `time` module
* Spotify playlist links

No external Python libraries are required.

## 🧠 How the Recommendation Works

The recommender uses three main inputs:

1. **Age**
2. **Gender**
3. **Mood**

### Age Groups

| Age      | Age Group |
| -------- | --------- |
| Below 25 | Youth     |
| 25–40    | Adult     |
| Above 40 | Senior    |

The program combines:

```text
Gender + Age Group + Mood
```

to select a corresponding Spotify playlist.

### Recommendation Flow

```text
Enter Age
     ↓
Enter Gender
     ↓
Select Mood
     ↓
Determine Age Group
     ↓
Match Gender + Age Group + Mood
     ↓
Select Spotify Playlist
     ↓
Open Spotify in Browser
```

## 🎭 Available Moods

The current version supports:

* **Happy**
* **Sad**
* **Angry**

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Gen-Music-Mood-Recommender.git
```

### 3. Open the Project Folder

```bash
cd Gen-Music-Mood-Recommender
```

### 4. Run the Program

```bash
python music_mood_recommender.py
```

### 5. Enter Your Details

The program will ask for:

```text
Enter your age:
Enter your gender (male/female):

Choose your current mood:
1. Happy
2. Sad
3. Angry
```

After selecting the mood, the program automatically opens the corresponding Spotify playlist.

## 💻 Example

```text
--- Welcome to the Gen-Music Mood Recommender ---

Enter your age: 21
Enter your gender (male/female): male

Choose your current mood:
1. Happy
2. Sad
3. Angry

Enter choice (1/2/3): 1

Detecting vibes for a 21 year old male feeling happy...

Opening a Spotify Playlist search for your mood, age group, and gender...
```

The selected Spotify playlist will then open automatically in the default browser.

## 🔮 Future Improvements

Future versions of this project could include:

* 🎵 More mood categories
* 🎼 More music genres
* 🎧 Individual song recommendations
* 🔗 Spotify API integration
* 🖥️ Graphical User Interface using Tkinter
* 🤖 Machine learning-based recommendations
* 🎤 Voice-based mood detection
* 📷 Facial-expression-based mood detection
* 💾 User preference history
* 📊 Recommendation analytics

## 📁 Project Structure

```text
Gen-Music-Mood-Recommender/
│
├── music_mood_recommender.py
├── README.md
└── .gitignore
```

## 👨‍💻 Author

**Harshal**

## ⭐ Project

If you find this project interesting, consider giving it a ⭐ on GitHub.
