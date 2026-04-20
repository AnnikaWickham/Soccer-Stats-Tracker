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
        fieldnames = ["date", "goals", "assists", "miles", "minuites"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stats)

def add_game(date, goals, assists, miles, minuites):
    stats = load_stats()
    stats.append({"date": date, "goals": goals, "assists": assists, "miles": miles, "minuites": minuites})
    save_stats(stats)
    print("Game added!")

def show_stats():
    stats = load_stats()
    if len(stats) == 0:
        print("No games yet.")
        return
    
    total_goals = sum(int(row["goals"]) for row in stats)
    total_assists = sum(int(row["assists"]) for row in stats)
    total_miles = sum(int(row["miles"]) for row in stats)
    total_minuites = sum(int(row["minuites"]) for row in stats)
    games_played = len(stats)
    
    print(f"\nGames played: {games_played}")
    print(f"Total goals: {total_goals}")
    print(f"Total assists: {total_assists}")
    print(f"Goals per game: {total_goals / games_played:.2f}")
    print(f"Assists per game: {total_assists / games_played:.2f}")
    print(f"Miles per game: {total_miles / games_played:.2f}")
    print(f"Minuites per game: {total_minuites / games_played:.2f}")

# Test it
def main():
    print("1. Add game")
    print("2. View stats")
    choice = input("Choose: ")
    
    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        goals = int(input("Goals: "))
        assists = int(input("Assists: "))
        miles = int(input("Miles Ran: "))
        minuites = int(input("Minuites Played: "))
        add_game(date, goals, assists, miles, minuites)
    elif choice == "2":
        show_stats()

main()
