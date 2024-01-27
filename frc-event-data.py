import requests
import json
import pandas as pd

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


# client.DefaultRequestHeaders.Accept.Clear();
# client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

api_url = "https://www.thebluealliance.com/api/v3/event/2019ncpem/rankings"
# api_url = "https://www.thebluealliance.com/api/v3/event/2024ncwak/rankings"
headers = {'User-Agent': 'Team 5607 Event Data CSV Generator', 'X-TBA-Auth-Key': ''}
response = requests.get(api_url, headers=headers)
response.json()

reff = pd.json_normalize(response.json()['rankings'])

df = pd.DataFrame(data=reff)

cmap = ListedColormap(['#0343df', '#e50000', '#ffff14', '#929591'])

ax = df.plot.bar(x='team_key', colormap=cmap)

ax.set_xlabel(None)
ax.set_ylabel('data')
ax.set_title('Team wins')
plt.show()