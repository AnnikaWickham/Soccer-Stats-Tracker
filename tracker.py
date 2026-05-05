import csv
import os

FILENAME = "stats.csv"

# Loads the current stats
def load_stats():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Writes the fields into the csv and whatever is passed in as "stats"
def save_stats(stats):
    with open(FILENAME, "w", newline="") as f:
        fieldnames = ["date", "goals", "assists", "miles", "minutes", "opponent", "score", "notes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stats)

# Method to write a new game into the stats.csv file
def add_game(date, goals, assists, miles, minutes, opponent, score, notes):
    stats = load_stats()
    stats.append({"date": date, "goals": goals, "assists": assists, "miles": miles, "minutes": minutes, "opponent": opponent, "score": score, "notes": notes})
    save_stats(stats)
    print("Game added!")

# Method to easily see current stats (for terminal / printed)
# (NOT used by ui.py)
def show_stats():
    stats = load_stats()
    if len(stats) == 0:
        print("No games yet.")
        return
    
    total_goals = sum(int(row["goals"]) for row in stats)
    total_assists = sum(int(row["assists"]) for row in stats)
    total_miles = sum(int(row["miles"]) for row in stats)
    total_minutes = sum(int(row["minutes"]) for row in stats)
    games_played = len(stats)
    
    print(f"\nGames played: {games_played}")
    print(f"Total goals: {total_goals}")
    print(f"Total assists: {total_assists}")
    print(f"Goals per game: {total_goals / games_played:.2f}")
    print(f"Assists per game: {total_assists / games_played:.2f}")
    print(f"Miles per game: {total_miles / games_played:.2f}")
    print(f"Minutes per game: {total_minutes / games_played:.2f}")
    
# Method to search and return for any game with the inputed opponent
def show_opponent(opponent_name):
    stats = load_stats()
    games = [row for row in stats if row["opponent"].lower() == opponent_name.lower()]
    return games

# Returns (playerGoals / teamGoals) to see a players total goal contribution
def get_goal_percentage():
    stats = load_stats()
    if len(stats) == 0:
        return ("No Current Stats")
    
    total_goals = sum(int(row["goals"]) for row in stats if row["score"] and "-" in row["score"])
    total_team_goals = sum(int(row["score"].split("-")[0]) for row in stats if row["score"] and "-" in row["score"])
    if total_team_goals == 0:
        return ("Error in Stats")

    return (f"{(total_goals / total_team_goals) * 100:.1f} %")

    

# (Used before ui.py was implemented)
def main():
    print("1. Add game")
    print("2. View stats")
    print("3. Look up opponent")
    choice = input("Choose: ")
    
    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        goals = int(input("Goals: "))
        assists = int(input("Assists: "))
        miles = int(input("Miles Ran: "))
        minutes = int(input("Minutes Played: "))
        opponent = input("Opponent: ")
        score = input("Score: ")
        notes = input("Notes: ")
        add_game(date, goals, assists, miles, minutes, opponent, score, notes)
    elif choice == "2":
        show_stats()
    elif choice == "3":
        opponent = input("Opponent name: ")
        show_opponent(opponent)

# To ensure tracker isnt called when first imported into ui.py
if __name__ == "__main__":
    main()
