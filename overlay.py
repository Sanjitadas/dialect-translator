# 📁 File: DialectApp/utils/overlay.py

import tkinter as tk
import threading

def show_subtitle_overlay(text):
    def run_overlay():
        root = tk.Tk()
        root.title("Live Subtitle")

        # Transparent & always-on-top overlay
        root.attributes('-topmost', True)
        root.geometry("800x100+100+50")
        root.overrideredirect(True)  # Remove window borders

        # Text display
        label = tk.Label(
            root,
            text=text,
            font=("Segoe UI", 20),
            fg="white",
            bg="black",
            wraplength=780,
            justify="center"
        )
        label.pack(expand=True, fill='both')

        # Close after 30 seconds or keep it open
        root.after(30000, root.destroy)
        root.mainloop()

    # Run overlay in a separate thread so it doesn't block Streamlit
    threading.Thread(target=run_overlay).start()
