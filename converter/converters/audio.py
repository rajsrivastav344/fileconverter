import subprocess
import os

def convert_audio(input_file, output_format, output_dir):
    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, base + "." + output_format)

    subprocess.run(
        ["ffmpeg", "-y", "-i", input_file, output_file],
        check=True
    )

    return output_file
