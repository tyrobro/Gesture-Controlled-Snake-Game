Gesture-Controlled Snake Game 🐍🖐️
This is the classic Snake game built in Python, but with a modern twist: you control it entirely with your hand!

Using your webcam, this program identifies your hand and translates your swipe gestures into commands for the snake. It uses Pygame for the game logic and OpenCV/MediaPipe for the computer vision.

🌟 Features
Gesture Control: Control the snake by swiping your hand (Up, Down, Left, Right) in front of your webcam.

Real-Time Hand Tracking: Uses Google's MediaPipe to find 21 landmarks on your hand and detect the direction of a fast swipe.

Live Camera Feed: A separate OpenCV window shows your live camera feed and the detected hand landmarks, so you can see what the computer sees.

Classic Game Logic: A complete Snake game built with Pygame, including collision detection, random fruit placement, and a "growing" snake body.

Scoring System: Includes a live score counter and a persistent high score that saves to highscore.txt.

Start Screen: The game waits for you to press the Spacebar before the action begins, giving you time to get ready.

💻 Tech Stack
Python 3

Pygame: For the game window, rendering, and logic.

OpenCV: To capture the webcam feed.

MediaPipe: For real-time hand tracking and landmark detection.

🚀 Setup & Installation
Follow these steps to get the game running on your local machine.

Clone the Repository

Bash
git clone https://github.com/YOUR-USERNAME/gesture-controlled-snake-game.git
cd gesture-controlled-snake-game
Create and Activate a Virtual Environment

Bash
# Create the environment
python3 -m venv venv

# Activate it (on macOS/Linux)
source venv/bin/activate

# (on Windows)
# .\venv\Scripts\activate
Install the Required Libraries All the necessary packages are in one simple command:

Bash
pip install pygame opencv-python mediapipe
🎮 How to Play
Run the main script from your terminal:

Bash
python3 main.py
Two windows will open: the game window (made with Pygame) and your camera feed (made with OpenCV).

The game window will show a "Press Space to Start" message.

Position your hand in the camera frame until you see the white landmark skeleton drawn over it.

Click on the game window to make it the active window, then press the Spacebar to begin the game.

Move the snake by swiping your hand in the desired direction. A short, quick swipe works best!

To quit the game, you can either click the 'X' on the game window or press 'q' while the camera window is active.