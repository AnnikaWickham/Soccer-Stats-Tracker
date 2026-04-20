import matplotlib.pyplot as plt
import csv

FILENAME = "stats.csv"

def load_stats():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

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
    plt.show()

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
    plt.show()

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
    plt.show()

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