import matplotlib.pyplot as plt
import csv

FILENAME = "stats.csv"

# Loads the current stats.csv file
def load_stats():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Creates a plot using pyplot to plot players goals over the course
# of the given games (time on x-axis) (# of goals on y-axis)
def plot_goals_over_time():
    stats = load_stats()
    dates = [row["date"] for row in stats]
    goals = [int(row["goals"]) for row in stats]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, goals, marker="o")
    plt.title("Goals Over Time")
    plt.xlabel("Date")
    plt.ylabel("Goals")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

# Creates a graph of minuites played over time
# (time on x-axis) (minuites per game on y-axis)
def plot_minutes_over_time():
    stats = load_stats()
    dates = [row["date"] for row in stats]
    minutes = [int(row["minutes"]) for row in stats]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, minutes, marker="o", color="orange")
    plt.title("Playing Time Over Time")
    plt.xlabel("Date")
    plt.ylabel("Minutes Played")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

# Graphs both goals scored and assists given on the same plot
# (time on x-axis) (goals - assists on y-axis)
def plot_goals_and_assists():
    stats = load_stats()
    dates = [row["date"] for row in stats]
    goals = [int(row["goals"]) for row in stats]
    assists = [int(row["assists"]) for row in stats]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, goals, marker="o", label="Goals")
    plt.plot(dates, assists, marker="s", label="Assists")
    plt.title("Goals and Assists Over Time")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

# Makes sure that charts.py isnt called when it first gets imported
# by ui.py, (this part was used before ui was implemented)
if __name__ == "__main__":
    print("1. Goals over time")
    print("2. Playing time over time")
    print("3. Goals and assists together")
    choice = input("Choose a graph: ")

    if choice == "1":
        plot_goals_over_time()
    elif choice == "2":
        plot_minutes_over_time()
    elif choice == "3":
        plot_goals_and_assists()