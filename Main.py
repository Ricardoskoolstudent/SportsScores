# Create an Intramural score tracker

SPH_NAME = 0
SPH_GP = 1
SPH_W = 2
SPH_L = 3
SPH_T = 4
SPH_GF = 5
SPH_GA = 6
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against
team=[SPH_NAME,0,0,0,0,0,0]
print("--- Welcome to the SportsScores Intramural Tracker ---")

# You will ask how many teams are playing.
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit

#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop