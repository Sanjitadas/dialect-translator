import threading

def show_subtitle_overlay(text):
    try:
        import tkinter as tk
    except ImportError:
        print("🪟 Warning: tkinter not available in this environment. Skipping subtitle overlay.")
        return

    def run_overlay():
        root = tk.Tk()
        root.title("Live Subtitle")

        root.attributes('-topmost', True)
        root.geometry("800x100+100+50")
        root.overrideredirect(True)

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

        root.after(30000, root.destroy)
        root.mainloop()

    threading.Thread(target=run_overlay).start()


