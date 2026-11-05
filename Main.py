# Create an Intramural score tracker
# Team List Contents:
# - Name[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)
# - Games Played[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span)
# - Wins[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)
# - Losses[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span)
# - Ties[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)
# - Goals For[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)
# - Goals Against[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)

teams = []
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.[span_20](start_span)[span_20](end_span).
num_teams = int(input("How many teams are playing? "))

# Loop that many times, create a team and set all scores to 0, then append it to your list of teams 0[span_21](start_span)[span_21](end_span)
for i in range(num_teams):
    name = input(f"Enter the name for team {i+1}: ")
    team = [name, 0, 0, 0, 0, 0, 0] #[span_22](start_span)[span_22](end_span)
    teams.append(team) #[span_23](start_span)[span_23](end_span)
print(teams)
# Start an infinite loop for main menu[span_24](start_span)[span_24](end_span)
while True:
    print("\nMenu Contents:")
    print("1. Add score")  # [span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)
    print("2. See Team stats")  # [span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span)
    print(
        "3. See Overall Standings")  # [span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span)
    print("4. Quit")  # [span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        # 1) Add score[span_31](start_span)[span_33](end_span)
        # Enter team 1, team 2, goals for team 1, goals for team 2[span_34](start_span)[span_34](end_span)[span_35](start_span)[span_35](end_span)
        t1_name = input("Enter team 1 name: ")
        t2_name = input("Enter team 2 name: ")
        t1_goals = int(input(f"Enter goals for {t1_name}: "))
        t2_goals = int(input(f"Enter goals for {t2_name}: "))

        team1 = []
        team2 = []
        # Find the teams[span_36](start_span)[span_36](end_span)[span_37](start_span)[span_37](end_span)
        for t in teams:
            if t[0].lower() == t1_name.lower():
                team1 = t
            if t[0].lower() == t2_name.lower():
                team2 = t
        if len(team1)==0 or len(team2)==0:
            print("Could not find both teams!")
        else:
            # Update the games played[span_38](start_span)[span_38](end_span)[span_39](start_span)[span_39](end_span)
            team1[1] += 1
            team2[1] += 1
            # Add goals for and goals against[span_40](start_span)[span_40](end_span)[span_41](start_span)[span_41](end_span)
            team1[5] += t1_goals
            team1[6] += t2_goals
            team2[5] += t2_goals
            team2[6] += t1_goals
            # Decide if it's a win, loss, or tie[span_42](start_span)[span_42](end_span)[span_43](start_span)[span_43](end_span)
        if t1_goals > t2_goals:
                team1[2] += 1 # Win for team 1
                team2[3] += 1 # Loss for team 2
        elif t2_goals > t1_goals:
                team2[2] += 1 # Win for team 2
                team1[3] += 1 # Loss for team 1
        else:
            team1[4] += 1 # Tie
            team2[4] += 1 # Tie
            print("Score successfully added!")
    # else:
    #         print("Error: One or both team names were not found.")
    elif choice == '2':
        # 2) See Team stats[span_44](start_span)[span_44](end_span)
        # Print a list of team names[span_45](start_span)[span_45](end_span)[span_46](start_span)[span_46](end_span)
        print("\nTeam Names:")
        for idx, t in enumerate(teams):
            print(f"{idx + 1}. {t[0]}")
    # Once the user selects, Print out their stats[span_47](start_span)[span_47](end_span)[span_48](start_span)[span_48](end_span)
    selection = int(input("Select a team number: ")) - 1
    if 0 <= selection < len(teams):
        sel_team = teams[selection]
        print(f"\nTeam: {sel_team[0]}")  # [span_49](start_span)[span_49](end_span)
        print(f"Games Played: {sel_team[1]}") #[span_50](start_span)[span_50](end_span)
        print(f"Wins: {sel_team[2]} Losses: {sel_team[3]} Ties: {sel_team[4]}")  # [span_51](start_span)[span_51](end_span)

#3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop