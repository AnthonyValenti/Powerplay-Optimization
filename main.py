import pandas as pd
import matplotlib.pyplot as plt
from hockey_rink import NHLRink

shots=pd.read_csv('shots_2022.csv')
teamCode='TOR'
allShotsAgainstTeam=shots[((shots['awayTeamCode'] == teamCode) | (shots['homeTeamCode'] == teamCode))&(shots['teamCode']!=teamCode)]
homeShotsAgainst5v4 = allShotsAgainstTeam[
    (allShotsAgainstTeam['homeTeamCode'] == teamCode) &
    (allShotsAgainstTeam['homeSkatersOnIce'] == 4) &
    (allShotsAgainstTeam['awaySkatersOnIce'] == 5)
]
awayShotsAgainst5v4 = allShotsAgainstTeam[
    (allShotsAgainstTeam['awayTeamCode'] == teamCode) &
    (allShotsAgainstTeam['awaySkatersOnIce'] == 4) &
    (allShotsAgainstTeam['homeSkatersOnIce'] == 5)
]
shotsAgainst5v4 = pd.concat([homeShotsAgainst5v4,awayShotsAgainst5v4])
goalsAgainst5v4 = shotsAgainst5v4[shotsAgainst5v4['goal']==1]

grouped = goalsAgainst5v4.groupby('goalieNameForShot')
goalie_split = {}
for goalieName, group_df in grouped:
    goalie_split[goalieName] = group_df

print(goalie_split["Ilya Samsonov"])
x=goalie_split["Ilya Samsonov"]["xCordAdjusted"].values
y=goalie_split["Ilya Samsonov"]["yCordAdjusted"].values
labels=goalsAgainst5v4["shooterName"].values

rink = NHLRink(rotation=270)
fig, axs = plt.subplots(1, 1, figsize=(12, 8))
rink.draw(display_range="ozone", ax=axs)
rink.scatter(x,y)
plt.show()