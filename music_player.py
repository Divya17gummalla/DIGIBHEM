import tkinter as tk
from player_controls import MusicPlayerControls

class MusicPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        
        self.controls = MusicPlayerControls(self.root)
        self.controls.pack()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MusicPlayerApp()
    app.run()
