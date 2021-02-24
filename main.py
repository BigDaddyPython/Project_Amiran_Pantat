#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Amiran
#Group Name: Attack on Python
#Class: PN2004J
#Date: 9/2/21
#Version: Data Analysis
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#import matplotlib for visualizing data
import matplotlib.pyplot as pit
#import matplotlib.pyplot as plt for displaying data
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthlyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################
def sortCountry(df):

  #display sorted dataframe for Europe Region 1985-1995
  print("\n\n" + "Europe region is being selected.")

  #display sorted dataframe based on given year range of region (1985 - 1995)
  print("The countries in the region are shown below.")
  print("Year range: 1985 - 1995" + "\n")
  eur_region = df.iloc[84:216, 20:31]
  df1 = df.iloc[84:216,0:2]
  result = df1.join(eur_region)
  print("Total number of countries:", str(len(result.columns) - 2) + "\n")
  print(result)

  #display the top 3 countries that visited Singapore over the span of 10 years
  print("\n" + "The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years:")
  eur_finalresult = df.iloc[84:216, 20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)

  print(eur_finalresult.to_string())

  return

  
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #read df file
  df = pd.read_csv('MonthlyVisitors.csv')

  #All of the regions 
  Regions = ['S.E.A', 'Asia-Pacific', 'South-Asia Pacific', 'Middle East', 'Europe', 'North America', 'Australia', 'Africa']
  print('\n\n', "Regions:", Regions)
  Region = input("Please enter a region: ")

  #Error checking for the region input
  while True:
    Yahallo = 0
    Region = str(Region)
    if Region in Regions:
      if Region == "S.E.A":
        eur_region = df.iloc[: ,2:9]
        Yahallo += 1
        break
      elif Region == "Asia-Pacific":
        ap_region = df.iloc[: ,9:14]
        Yahallo += 1
        break
      elif Region == "South-Asia Pacific":
       sap_region = df.iloc[: ,14:17]
       Yahallo += 1
       break
      elif Region == "Middle East":
        me_region = df.iloc[: ,17:20]
        Yahallo += 1
        break
      elif Region == "Europe":
        eu_region = df.iloc[: ,20:31]
        Yahallo += 1
        break
      elif Region == "North America":
        na_region = df.iloc[: ,31:33]
        Yahallo += 1
        break
      elif Region == "Australia":
        aus_region = df.iloc[: ,33:35]
        Yahallo += 1
        break
      elif Region == "Africa":
        af_region = df.iloc[: ,35:36]
        Yahallo += 1
        break
    else:
      print("Region is invalid.")
      break
       
  
  #Error checking for the year input(For few regions only)
  if Yahallo >= 1:
    Years = ['1978-1987', '1988-1997', '1998-2007', '2008-2017']
    print('\n\n',Years)

    while True:
      Year = input('\n\n' + "Please enter the year:")
      try:
        Year = int(Year)
      except:
        print("Invalid format.")
        break
      else:
        if Year == 1978 and Region == 'S.E.A':
          SEA = df.iloc[:120,:9]
          reg_df = df.iloc[:120,2:9]
          print("Total number of countries:", str(len(SEA.columns) - 2))
          print(SEA)
          Yahallo += 1
          break
        elif Year == 1978 and Region == 'Asia-Pacific':
          years = df.iloc[:120,0:2]
          reg_df = df.iloc[:120, 9:14]
          total = years.join(reg_df)
          print("Total number of countries:", str(len(reg_df.columns) - 2))
          print(total)
          Yahallo += 1
          break
        elif Year == 1978 and Region == 'South-Asia Pacific':
          years = df.iloc[:120,0:2]
          reg_df = df.iloc[:120,14:17]
          total = years.join(reg_df)
          print("Total number of countries:", str(len(SEA.columns) - 2))
          print(total)
          Yahallo += 1
          break
        else:
          print("Invalid year. Please enter a valid year.")
          break


  #Pie chart and colours for Europe region only      
  if Yahallo >= 2:
    countries = ['United Kingdom', 'Germany', 'France', 'Italy', 'Netherlands', 'Greece', 'Belgium & Luxembourg', 'Switzerlands', 'Austria', 'Scandanavia', 'CIS & Eastern Europe']
    slices = [2834621, 1522806, 709847,531890,715570,155202,177584,582608,180468,818596,397623]
    colours = ['#FFCA33', '#93FF33', '#33FFB2','#33FFE9', '#33A8FF','#3346FF','#9033FF','#DD33FF', '#FF33CE', '#FF00CE', '#FF3346']

    pit.pie(slices,
        labels=countries,
        startangle=90,
        colors=colours,
        shadow=False,
        explode=(0.1,0.1,0.1,0.1,0,0,0,0,0,0,0),
        autopct='%1.2f%%')

    pit.show()

#########################################################################
#Main Branch: End of Code
#########################################################################