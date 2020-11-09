from visual import visualize
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import seaborn as sns

sns.set(style="darkgrid")
"""url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_area_type_hosp_dynamics.csv'
r = requests.get(url, allow_redirects=True)
open('covid19_by_area_type_hosp_dynamics.csv', 'wb').write(r.content)"""

df = pd.read_csv("covid19_by_area_type_hosp_dynamics.csv", sep=',')
dfL = df[df['registration_area'] == 'Львівська']
dfV = df[df['registration_area'] == 'Вінницька']
dfD = df[df['registration_area'] == 'Дніпропетровська']

data = df.groupby(
    ['zvit_date']
).agg(
    {
        'new_susp': "sum",
        'new_confirm': "sum",
        'active_confirm': "sum",
        'new_death': "sum",
        'new_recover': "sum",
    }
)


death = df.groupby(['registration_area']
                   ).agg(
    {
        'new_death': "sum",
    }
)
active = df.groupby(['registration_area']
                   ).agg(
    {
        'active_confirm': "sum",
    }
)
#death.to_excel("death_by_area.xlsx")
#visualize(data, ["new_susp", "new_confirm", "active_confirm", "new_death", "new_recover"])
visualize(active, ["active_confirm"])


nb = 'ukr_admbnda_adm1_q2_sspe_20171221.shp'
regions = gpd.read_file(nb)
regions['registration_area'] = regions['ADM1_UA']
merged = regions.set_index('registration_area').join(death)
merged = merged.reset_index()
merged = merged.fillna(0)
fig, ax = plt.subplots(1, figsize=(40, 20))
ax.axis('off')
ax.set_title('Heat Map of deaths', fontdict={'fontsize': '40', 'fontweight': '3'})

color = 'Oranges'
vmin, vmax = 0, 231
sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
cbar.ax.tick_params(labelsize=20)
merged.plot('new_death', cmap=color, linewidth=0.8, ax=ax, figsize=(40, 20))
plt.show()
