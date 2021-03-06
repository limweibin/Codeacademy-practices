import pandas as pd
import matplotlib.pyplot as plt
#Script of Data visualisation for data with regards to roller coasters obtained from 2013-2018 Golden Ticket Awards as part of codeacademy practice
# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(wood)




# write function to plot rankings over time for 1 roller coaster here:
def rankings(name,ranking,parkname):
  new_ranking = ranking[(ranking.Name == name) & (ranking.Park == parkname)]
  plt.plot(new_ranking['Year of Rank'],new_ranking['Rank'])
  plt.xlabel('Year Awarded')
  plt.ylabel('Ranking of Roller Coaster')  
  plt.title('Ranking of {} from {} over time'.format(name,parkname))

  plt.show()

rankings('El Toro', wood,'Six Flags Great Adventure')


plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def rankings2(name1,name2,parkname1,parkname2,ranking):
  new_ranking = ranking[(ranking.Name == name1)& (ranking.Park == parkname1)]
  new_ranking2 = ranking[(ranking.Name ==name2)& (ranking.Park == parkname2)]
  plt.plot(new_ranking['Year of Rank'],new_ranking['Rank'], color = 'green')
  plt.plot(new_ranking2['Year of Rank'],new_ranking2['Rank'],color = 'blue')
  plt.xlabel('Year Awarded')
  plt.ylabel('Ranking of Roller Coaster')
  plt.title('Rankings for {} from {}\n and {} from {} over time'.format(name1,parkname1,name2,parkname2))
  plt.legend(['{} from {}'.format(name1,parkname1),'{} from {}'.format(name2,parkname2)])
  plt.show()

rankings2('El Toro','Boulder Dash','Six Flags Great Adventure','Lake Compounce',wood)

plt.clf()

# write function to plot top n rankings over time here:
def topnrankings(n,ranking):
  new_ranking = ranking[ranking['Rank']<= n]
  a = new_ranking.drop_duplicates(subset = ['Name'],keep='last')
  for i in range(len(a)):
    plot_data = ranking[(ranking['Name']==a.iloc[i][1]) & (ranking['Park']==a.iloc[i][2])]
    plt.plot(plot_data['Year of Rank'],plot_data['Rank'])
  plt.xlabel('Year Awarded')
  plt.ylabel('Ranking')
  plt.legend(a.Name,prop={'size': 9})
  plt.show()
  plt.title('Ranking of top {} coasters over time'.format(n))
topnrankings(5,wood)

plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')

# write function to plot histogram of column values here:
def histogram(df,name):
  df = df.dropna(subset = [name])
  plt.hist(df[name],bins = 100)
  plt.ylabel('Amount of roller coasters')
  plt.xlabel('{} of the roller coasters'.format(name))
  plt.title('{} of the roller coasters'.format(name))
  plt.show()
histogram(roller_coasters,'length')

plt.clf()

# write function to plot inversions by coaster at a park here:
def barchart(df,name):
  new_rows = df[df.park == name]
  plt.figure(figsize=(25,10))
  plt.bar(range(len(new_rows)), new_rows['num_inversions'])
  ax = plt.subplot()
  ax.set_xticks(range(len(new_rows)))
  ax.set_xticklabels(new_rows.name)
  plt.ylabel('Num inversions of {}'.format(name))
  plt.title('Bar chart of number of inversions for roller coasters')
  plt.show()
barchart(roller_coasters,'Parc Asterix')

plt.clf()

# write function to plot pie chart of operating status here:
def piechart(df):
  plt.figure(figsize=(5,5))
  operating = df[df.status == 'status.operating']
  closed = df[df.status == 'status.closed.definitely']
  number_of_operating = len(operating)
  number_of_closed = len(closed)
  data = [len(operating),len(closed)]
  plt.pie(data,labels = ['operating','closed'],colors = ['lightskyblue','green'],autopct = '%0.2f')
  plt.title('Percentage of operating vs closed roller coasters \n out of {} roller coasters'.format(str(len(df))))
  plt.show()
piechart(roller_coasters)

plt.clf()

# write function to create scatter plot of any two numeric columns here:
def scatterplot(df,column1,column2):
  plt.scatter(df[column1],df[column2],alpha=0.5)
  plt.xlabel('{} of roller coasters'.format(column1))
  plt.ylabel('{} of roller coasters'.format(column2))
  plt.title('Scatter plot of {} vs {}'.format(column1,column2))
  plt.show()
scatterplot(roller_coasters,'speed','height')

plt.clf()
