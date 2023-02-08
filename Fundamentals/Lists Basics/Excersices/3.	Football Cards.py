cards = input().split()
terminate = False

team_a_off_players = []
team_b_off_players = []

for card in cards:
    if card in team_a_off_players or card in team_b_off_players:
        continue

    card_args = card.split('-')
    team = card_args[0]
    number = card_args[1]

    if team == 'A':
        team_a_off_players.append(card)
    else:
        team_b_off_players.append(card)

    if len(team_a_off_players) > 4 or len(team_b_off_players) > 4:
        terminate = True
        break

print(f"Team A - {11 - len(team_a_off_players)}; Team B - {11 - len(team_b_off_players)}")


if terminate:
    print("Game was terminated")
