import subprocess
import os

def convert_audio(input_file, output_format):
    output_file = os.path.splitext(input_file)[0] + "." + output_format
    subprocess.run([
        "ffmpeg", "-y", "-i", input_file, output_file
    ], check=True)
    return output_file
