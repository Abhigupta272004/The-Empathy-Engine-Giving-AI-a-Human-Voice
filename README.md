# 🎙️ Empathy Engine – Emotion-Aware Text-to-Speech

## 📌 Project Description

The **Empathy Engine** is a Python-based application that converts text into emotionally expressive speech.
It bridges the gap between plain text and human-like voice by detecting the **emotion of input text** and dynamically modifying **voice parameters** such as speech rate, pitch, and volume.

---

## 🎯 Objective

To design and build a system that:

* Detects emotion from input text
* Maps emotion to voice characteristics
* Generates expressive audio output

---

## ⚙️ How to Run the Project

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd empathy-engine
```

### 2. Install Dependencies

```bash
pip3 install flask vaderSentiment
```

### 3. Install FFmpeg (Mac)

```bash
brew install ffmpeg
```

### 4. Run Application

```bash
python3 app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧠 Design Choices & Implementation

### 🔹 Emotion Detection

* Implemented using **VADER Sentiment Analysis**
* Classifies text into:

  * Very Positive
  * Positive
  * Neutral
  * Negative
  * Very Negative

---

### 🔹 Emotion → Voice Mapping Logic

| Emotion       | Speech Rate     | Pitch               | Volume   |
| ------------- | --------------- | ------------------- | -------- |
| Very Positive | Fast            | Increased           | High     |
| Positive      | Moderately Fast | Slightly High       | Medium   |
| Neutral       | Normal          | Default             | Normal   |
| Negative      | Slow            | Lowered             | Low      |
| Very Negative | Very Slow       | Significantly Lower | Very Low |

---

### 🔹 Voice Modulation

* **Speech Generation:** macOS `say` command
* **Pitch & Volume Control:** Applied using FFmpeg audio filters
* **Rate Adjustment:** Controlled via TTS engine

---

### 🔹 Audio Output

* Output format: **MP3**
* Files stored in:

  ```
  static/audio/
  ```
* Audio is:

  * Played in browser
  * Available for download

---

### 🔹 User Interface

* Built using HTML, CSS, and JavaScript
* Features:

  * Text input + microphone input
  * Emotion display with emoji
  * Dynamic background based on emotion
  * Audio waveform animation
  * Download button

---

## 📦 Project Structure

```
empathy-engine/
│── app.py
│── emotion_engine.py
│── tts_engine.py
│── static/
│    └── audio/
│── templates/
│    └── index.html
```

---

## 💡 Key Features

* Emotion detection from text
* Dynamic voice modulation
* Real pitch and volume adjustment
* Web-based interface
* Audio playback and download
* Emotion-aware UI

---

## 🚀 Bonus Implementations

* Emotion intensity visualization
* Microphone input support
* Dynamic UI changes based on emotion
* Waveform animation during playback

---

## 🧪 Example Input

```
I am extremely happy today!
```

### Output:

* Emotion: Positive
* Faster speech rate
* Higher pitch
* Louder volume
* Generated expressive audio

---

## 👨‍💻 Author

Abhi Gupta

---

## 📌 Notes

This project fulfills all required deliverables:

* ✔ Accepts text input
* ✔ Detects emotion
* ✔ Modulates voice parameters
* ✔ Maps emotion to voice
* ✔ Generates playable audio output

---

## ⭐ Conclusion

The Empathy Engine demonstrates how combining **Natural Language Processing** and **Audio Processing** can create more human-like AI communication systems.
