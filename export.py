# 📁 File: DialectApp/utils/export.py

import os
from datetime import datetime

def export_transcript(text: str):
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"transcript_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
