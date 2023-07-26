import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('fifa21 raw data v2.csv', low_memory = False)
df.head()
df.columns
df[['Height', 'Weight']].dtypes
df['Height'].unique()
def convert_cm(height):
    if 'cm' in height:
        return float(height.replace('cm', ''))
    else:
        feet, inches = height.split('\'')
        feet = float(feet)
        inches = float(inches.replace('"', ''))
        return (feet * 30.48) + (inches * 2.54)
df['Height'] = df['Height'].apply(convert_cm)
df['Height'].unique()
df['Weight'].unique()
def convert_kg(weight):
    if 'kg' in weight:
        return float(weight.replace('kg', ''))
    else:
        return round(float(weight.replace('lbs', '')) / 2.2, 2)
df['Weight'] = df['Weight'].apply(convert_kg)
df['Weight'].unique()
df['Joined'].head()
df[['Month' ,'Day-Year']] = df['Joined'].str.split(' ', n = 1, expand = True)
df[['Day', 'Year']] = df['Day-Year'].str.split(',', n = 1, expand = True)
df.drop(columns=['Joined', 'Day-Year'], axis = 1)
df[['Month', 'Day', 'Year']].head()
df[['Value', 'Wage', 'Release Clause']].head()
df[['Value', 'Wage', 'Release Clause']].isna().sum()
df[['Value', 'Wage', 'Release Clause']].isnull().sum()
def convert_money(money):
    if 'M' in money:
        return float(money.replace('€', '').replace('M', '')) * 1e6
    elif 'K' in money:
        return float(money.replace('€', '').replace('K', '')) * 1e3
    else:
        return float(money.replace('€', ''))
df['Value'] = df['Value'].apply(convert_money)
df['Wage'] = df['Wage'].apply(convert_money)
df['Release Clause'] = df['Release Clause'].apply(convert_money)
df[['Value', 'Wage', 'Release Clause']].head()
df['Hits']
df['Hits'] = df['Hits'].str.replace('\n', '')
df['Hits']
No_of_players= df.groupby(['Nationality']).size().sort_values(axis = 0, ascending = False)
No_of_players.head(10)
No_of_players.head(10).plot(kind='bar',color='brown')
plt.xlabel("Nationality")
plt.ylabel("Number of players")
plt.title("Nationality of Players")
plt.show()
Age_of_players= df.groupby(['Age']).size().sort_values(axis = 0, ascending = False)
Age_of_players.plot(kind='bar',color='orange')
plt.xlabel("Age")
plt.ylabel("Number of players")
plt.title("Age of Players")
plt.show()
Number_of_hits = df.groupby(['Name']).size().sort_values(axis = 0,ascending = False)
Number_of_hits.head(10).plot(kind='bar',color='green')
plt.xlabel("Name")
plt.ylabel("Hits")
plt.title("Number of Hits")
plt.show()
Best_players = df.sort_values(['↓OVA', 'Hits'],ascending=[False, False]).head(10)
Top= Best_players[['Name', '↓OVA', 'Hits']]
Top_players=Top.head(10)
Top_players
def remove_n(team):
    if '\n' in team:
        return team.replace('\n', '')
df['Club'] = df['Club'].apply(remove_n)
Teams = df['Club'].value_counts() 
Teams.count()
best_players = df.sort_values('↓OVA',ascending = False).head(100)
best_players.head()
Team_vals = best_players['Club'].value_counts()
Team_vals.count()
Team_vals.plot(kind="bar",color='purple');
plt.title("Club with Best Players");
plt.xlabel(" Club Names")
plt.ylabel("Number of Best Players")
plt.show()
