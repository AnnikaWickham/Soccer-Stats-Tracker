import tkinter as tk
import tkinter.messagebox
from tracker import load_stats, add_game, show_opponent, get_goal_percentage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from charts import plot_goals_over_time, plot_minutes_over_time, plot_goals_and_assists

root = tk.Tk()
root.title("Soccer Performance Tracker")
root.geometry("500x400")

label = tk.Label(root, text="Soccer Performance Tracker", font=("Arial", 18, "bold"))
label.pack(pady=20)

def open_add_game():
    form = tk.Toplevel(root)
    form.title("Add Game")
    form.geometry("400x600")

    fields = ["Date (YYYY-MM-DD)", "Goals Scored By You", "Assists From You", "Miles Ran", "Minutes Played", "Opponent", "Score (YourTeam - OtherTeam)", "Notes"]
    entries = {}

    for field in fields:
        tk.Label(form, text=field).pack(pady=2)
        entry = tk.Entry(form, width=30)
        entry.pack(pady=2)
        entries[field] = entry

    def submit():
        add_game(
            entries["Date (YYYY-MM-DD)"].get(),
            int(entries["Goals Scored By You"].get()),
            int(entries["Assists From You"].get()),
            int(entries["Miles Ran"].get()),
            int(entries["Minutes Played"].get()),
            entries["Opponent"].get(),
            entries["Score (YourTeam - OtherTeam)"].get(),
            entries["Notes"].get()
        )
        form.destroy()
        tk.messagebox.showinfo("Success", "Game added!")
    tk.Button(form, text="Submit", width=20, command=submit).pack(pady=20)

def open_charts():
    form = tk.Toplevel(root)
    form.title("Performance Charts")
    form.geometry("600x500")

    def show_chart(chart_func):
        for widget in form.winfo_children():
            widget.destroy()
        
        fig = chart_func()
        canvas = FigureCanvasTkAgg(fig, master=form)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    btn_frame = tk.Frame(form)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Goals Over Time", command=lambda: show_chart(plot_goals_over_time)).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Playing Time", command=lambda: show_chart(plot_minutes_over_time)).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Goals & Assists", command=lambda: show_chart(plot_goals_and_assists)).pack(side=tk.LEFT, padx=5)

def open_stats():
    form = tk.Toplevel(root)
    form.title("Soccer Stats")
    form.geometry("400x600")    

    stats = load_stats()
    if len(stats) == 0:
        tk.Label(form, text="No Recorded Games").pack(pady=2)
    else: 
        total_goals = sum(int(row["goals"]) for row in stats)
        total_assists = sum(int(row["assists"]) for row in stats)
        total_miles = sum(int(row["miles"]) for row in stats)
        total_minutes = sum(int(row["minutes"]) for row in stats)
        games_played = len(stats)
        tk.Label(form, text=f"\nGames played: {games_played}").pack(pady=2)
        tk.Label(form, text=f"Total goals: {total_goals}").pack(pady=2)
        tk.Label(form, text=f"Total assists: {total_assists}").pack(pady=2)
        tk.Label(form, text=f"Goals per game: {total_goals / games_played:.2f}").pack(pady=2)
        tk.Label(form, text=f"Assists per game: {total_assists / games_played:.2f}").pack(pady=2)
        tk.Label(form, text=f"Miles per game: {total_miles / games_played:.2f}").pack(pady=2)
        tk.Label(form, text=f"Minutes per game: {total_minutes / games_played:.2f}").pack(pady=2)
        tk.Label(form, text=f"Total Minuites: {total_minutes}").pack(pady=2)
        tk.Label(form, text=f"Total Miles: {total_miles}").pack(pady=2)
        tk.Label(form, text=f"Personal Goal Percentage: {get_goal_percentage()}").pack(pady=2)

def look_up_opponent():
    form = tk.Toplevel(root)
    form.title("Search Game by Opponent")
    form.geometry("400x600")

    tk.Label(form, text="Opponent").pack(pady=2)
    entry = tk.Entry(form, width=30)
    entry.pack(pady=2)

    results_frame = tk.Frame(form)
    results_frame.pack(pady=10)

    def search():
        for widget in results_frame.winfo_children():
            widget.destroy()
        
        games = show_opponent(entry.get())
        
        if len(games) == 0:
            tk.Label(results_frame, text="No games found").pack()
        else:
            for game in games:
                tk.Label(results_frame, text=f"{game['date']} | {game['score']} | Goals: {game['goals']} | Assists: {game['assists']}").pack()
                tk.Label(results_frame, text=f"Notes: {game['notes']}").pack(pady=2)

    tk.Button(form, text="Search", width=20, command=search).pack(pady=20)

    

add_button = tk.Button(root, text="Add Game", width=20, height=2, command= open_add_game)
add_button.pack(pady=5)

stats_button = tk.Button(root, text="View Stats", width=20, height=2, command= open_stats)
stats_button.pack(pady=5)

charts_button = tk.Button(root, text="View Charts", width=20, height=2, command=open_charts)
charts_button.pack(pady=5)

opponent_button = tk.Button(root, text="Look Up Opponent", width=20, height=2, command = look_up_opponent)
opponent_button.pack(pady=5)


root.mainloop()