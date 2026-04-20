import csv
import os

FILENAME = "stats.csv"

def load_stats():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_stats(stats):
    with open(FILENAME, "w", newline="") as f:
        fieldnames = ["date", "goals", "assists"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stats)

def add_game(date, goals, assists):
    stats = load_stats()
    stats.append({"date": date, "goals": goals, "assists": assists})
    save_stats(stats)
    print("Game added!")

# Test it
add_game("2025-04-20", 2, 1)
print(load_stats())
