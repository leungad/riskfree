
import requests
import pandas as pd
from bs4 import BeautifulSoup



def rf_rate(country):
    country = country.title()
    ## Find default spread for country, create dataframe ##
    website_url = requests.get('http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html').text
    soup = BeautifulSoup(website_url,'lxml')
    My_table = soup.find('table')

    ## Create Table from scraped data ##
    table_tag = soup.select("table")[0]
    tab_data = [[item.text for item in row_data.select("th,td")]
                    for row_data in table_tag.select("tr")]
    df = pd.DataFrame(tab_data,columns=pd.DataFrame(tab_data).iloc[0,:]).drop(0,axis=0)

    df = df.replace('\n','', regex=True)
    df.Country = df.Country.str.replace("     ", "")

    ##  Locate 10-Year Governemnt Bond Yield ##
    website_url = requests.get('http://www.worldgovernmentbonds.com/spread-historical-data/').text
    soup1 = BeautifulSoup(website_url,'lxml')

    ## Create Table from scraped data ##
    table_tag = soup1.select("table")[0]
    tab_data1 = [[item.text for item in row_data.select("th,td")]
                    for row_data in table_tag.select("tr")]
    df1 = pd.DataFrame(tab_data1,columns=pd.DataFrame(tab_data1).iloc[0,:]).drop(0,axis=0)
    df1 = df1.replace('\n','', regex=True).drop(1,axis=0)
    df1.columns = ['','Country','10Y Yield','','Ger','Usa','Chi','Aus','c']
    df1 = df1.drop('c',axis=1)


    ## Calculate the risk free rate from the loc'ed values ##
    adj_spread = float(df[df.Country == country].loc[:,'Adj. Default Spread'].values[0][:-1])
    ten_yield = float(df1[df1.Country == country].loc[:,'10Y Yield'].values[0][:-1])
    rf = (ten_yield - adj_spread)/100

    return(rf)

