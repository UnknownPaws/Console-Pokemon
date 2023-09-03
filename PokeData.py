import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Pokemon.csv', index_col=0)
print(df.head())
sns.lmplot(x='Defense', y='Attack', data=df, hue='Stage', fit_reg=False) #lmplot works on the figure level, so one can not have a different grah in the same window (figure) as lmplot

plt.figure()
plt.subplot(2,2,1) #first graph in 2x2 figure
sns.regplot(x='Defense', y='Attack', data=df)

plt.subplot(222) #second graph in 2x2 figure
metrics = df.drop(['Total', 'Stage', 'Legendary'], axis=1) #rows are axis=0 and columns are axis=1
sns.boxplot(data=metrics)

plt.subplot(223) #3rd axes in the 2x2 figure
pokePalet = ['#00A817', #Grass green
             '#FA4602', #Fire red
             '#02D0FA', #Waer blue
             '#716753', #Bug brown
             '#5A5854', #Normal grey
             '#6DD222', #Poison green
             '#0E36D5', #Electric blue
             '#A9650D', #Ground brown
             '#FDFF0A', #Fairy yellow
             '#CA0202', #Fighting red
             '#FF8407', #Psychic orange
             '#303030', #Rock grey
             '#E5E5E5', #Ghost white
             '#00EFFF', #Ice blue
             '#F30953'] #Dragon flaming pink
sns.violinplot(x='Type 1', y='Attack', data=df, palette=pokePalet)

plt.subplot(224) #4th axes in 2x2 figure
sns.swarmplot(x='Type 1', y='Attack', data=df, palette=pokePalet)

plt.figure()
pokePalet2 = ['#0E36D5', '#E5E5E5', '#FA4602']
sns.violinplot(x='Stage', y='Attack', data=df, palette=pokePalet2, inner=None)
sns.swarmplot(x='Stage', y='Attack', data=df, color='k', alpha=0.7) #k means black, aplha changes transperency (0-1)


plt.figure(figsize=(10,10))
plt.subplot(221)
cor = metrics.corr()
sns.heatmap(cor)
print(cor)

plt.subplot(222)
sns.distplot(df.Attack)

plt.subplot(223)
sns.countplot(x='Type 1',data=df, palette=pokePalet)

plt.subplot(224)
sns.barplot(x='Type 1', y='Attack', data=df, palette=pokePalet) #Averages values by default

waterPoke = df[df['Type 1'] == 'Water']
print(np.mean(waterPoke.Attack))


plt.figure()

plt.subplot(211)
sns.kdeplot(df.Attack, df.Defense)

plt.subplot(212)
sns.jointplot(df.Attack, df.Defense)

g = sns.factorplot(x='Type 1',
                   y='Attack',
                   data=df,
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot 
g.set_xticklabels(rotation=45)

plt.show()