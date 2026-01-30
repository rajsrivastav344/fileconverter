import os
from flask import Flask, render_template, request, send_file
from converters.audio import convert_audio
from converters.video import convert_video
from converters.image import convert_image
from converters.document import convert_document

app = Flask(__name__)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMAGE = {"jpg","jpeg","png","webp","bmp","tiff","ico"}
DOCUMENT = {
    "doc","docx","ppt","pptx","xls","xlsx",
    "odt","ods","odp","pdf"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        target_format = request.form["format"]

        input_path = os.path.join(UPLOAD_DIR, file.filename)
        file.save(input_path)

        ext = file.filename.split(".")[-1].lower()

        # Conversion logic with correct indentation
        if ext in {"mp3","wav","flac","aac","ogg"}:
            output = convert_audio(input_path, target_format, OUTPUT_DIR)
        elif ext in {"mp4","mkv","avi","webm","mov","flv"}:
            output = convert_video(input_path, target_format, OUTPUT_DIR)
        elif ext in IMAGE:
            output = convert_image(input_path, target_format, OUTPUT_DIR)
        elif ext in DOCUMENT:
            output = convert_document(input_path, target_format, OUTPUT_DIR)
        else:
            return "Unsupported file type"

        return render_template("result.html", file=output)

    return render_template("index.html")


@app.route("/download/<path:filename>")
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
