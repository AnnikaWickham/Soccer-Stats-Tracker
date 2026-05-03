import tkinter as tk
from tracker import load_stats, add_game, show_opponent

root = tk.Tk()
root.title("Soccer Performance Tracker")
root.geometry("500x400")

label = tk.Label(root, text="Soccer Performance Tracker", font=("Arial", 18, "bold"))
label.pack(pady=20)

add_button = tk.Button(root, text="Add Game", width=20, height=2)
add_button.pack(pady=5)

stats_button = tk.Button(root, text="View Stats", width=20, height=2)
stats_button.pack(pady=5)

opponent_button = tk.Button(root, text="Look Up Opponent", width=20, height=2)
opponent_button.pack(pady=5)

root.mainloop()