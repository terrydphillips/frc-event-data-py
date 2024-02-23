import requests
import json
import pandas as pd

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

# URL to GET
api_url = "https://www.thebluealliance.com/api/v3/event/2019ncpem/rankings"
# api_url = "https://www.thebluealliance.com/api/v3/event/2024ncwak/rankings"

# Put your TBA auth key in the last set of quotes
headers = {'User-Agent': 'Team 5607 Event Data CSV Generator', 'X-TBA-Auth-Key': ''}
response = requests.get(api_url, headers=headers)

# Dumps all of the JSON contents of the GET
response.json()

reff = pd.json_normalize(response.json()['rankings'])

df = pd.DataFrame(data=reff)

# Select columns from the data frame
df1 = df[['team_key','record.wins']]

cmap = ListedColormap(['#0343df', '#e50000', '#ffff14', '#929591'])

# Plot 
ax = df1.plot.bar(x='team_key', colormap=cmap)
ax.set_xlabel('Team number')
ax.set_ylabel('Team wins')
ax.set_title('Team wins')
plt.show()
