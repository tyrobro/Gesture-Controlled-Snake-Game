# Gesture-Controlled Snake Game 🐍🖐️

This is the classic Snake game built in Python, but with a modern twist: **you control it entirely with your hand!**

Using your webcam, this program identifies your hand and translates your swipe gestures into commands for the snake. It uses Pygame for the game logic and OpenCV/MediaPipe for the computer vision.



---

## 🌟 Core Features

| Feature | Description |
| :--- | :--- |
| **Gesture Control** | Control the snake by swiping your hand (Up, Down, Left, Right) in front of your webcam. |
| **Real-Time Hand Tracking** | Uses Google's MediaPipe to find 21 landmarks on your hand and detect the direction of a fast swipe. |
| **Live Camera Feed** | A separate OpenCV window shows your live camera feed and the detected hand landmarks. |
| **Classic Game Logic** | A complete Snake game built with Pygame, including collision detection, random fruit placement, and a "growing" snake body. |
| **Scoring System** | Includes a live score counter and a persistent high score that saves to `highscore.txt`. |
| **Start Screen** | The game waits for you to press the **Spacebar** before the action begins. |

---

## 💻 Tech Stack

* **Python 3**
* **Pygame:** For the game window, rendering, and logic.
* **OpenCV:** To capture the webcam feed.
* **MediaPipe:** For real-time hand tracking and landmark detection.

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/tyrobro/Gesture-Controlled-Snake-Game.git](https://github.com/tyrobro/Gesture-Controlled-Snake-Game.git)
cd Gesture-Controlled-Snake-Game
