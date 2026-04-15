from flask import Flask, render_template, request, send_file
from emotion_engine import detect_emotion
from tts_engine import speak

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    emotion = None

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            emotion = detect_emotion(text)
            audio_file = speak(text, emotion)

    return render_template("index.html", audio_file=audio_file, emotion=emotion)

@app.route("/download")
def download():
    file_path = request.args.get("file")
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)