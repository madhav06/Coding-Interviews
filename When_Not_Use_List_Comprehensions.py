
# When should you not use a list comprehension?

# Two common cases where you shouldn't use a list:

# - you don't actually want a list
# - the logic is too long.

#Case2: when logic is too long.

# active_player_accounts = [player.get_account() for team in league_teams
#     if len(team.roster) > 1 for player in team.get_players()
#     if not player.is_injured()]


# this piece is still hard to understand, we can make it somewhat more readable:

active_player_accounts = []

for team in league_teams:

	# teams need to have at least 2 players before they are considered active

	if len(team.roster) <= 1:

		continue

	for player in team.get_players():

		# only want active players

		if players.is_injured():
			continue

		account = player.get_account()
		active_player_accounts.append(account)