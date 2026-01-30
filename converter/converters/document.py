import subprocess
import os

def convert_document(input_file, output_format, output_dir):
    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            output_format,
            input_file,
            "--outdir",
            output_dir
        ],
        check=True
    )

    base = os.path.splitext(os.path.basename(input_file))[0]
    return os.path.join(output_dir, base + "." + output_format)
