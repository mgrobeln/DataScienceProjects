#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:00:05 2020

@author: Marlena
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd


# List of item names to search on eBay (can add upt to 5 MAX)
name_list = ["Python Textbook", "Ramen","Nespresso capsules","Air pods apple","audio technica headphones"]
all_data=[]

item_name=[]
prices=[] 

# Returns a list of urls that search eBay for an item
def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
    urls=[]
    for name in names:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
        
        
        #by adding this ending to the url we ensure that we are only looking at "NEW" items and we are looking at 200 items
        url = url + name.replace(" ", "+")+ "&rt=nc&LH_ItemCondition=3&_ipg=200" 
        urls.append(url)
    # Returns the list of completed urls
    return urls




def ebay_scrape(urls,name):
    
    i=0
    for url in urls:
        #erase values from previous run to avoid duplicate values in our list
        item_name[:]=[]
        prices[:] =[]
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')
        
        
        #finding all products that contain specified 'name_list' key word
        listings = soup.find_all('li', attrs={'class': 's-item'})
        
        
 
        for listing in listings:
            
            
            prod_name=" "
            prod_price = " "
            for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
                if(str(name.find(text=True, recursive=False))!="None"):
                    prod_name=str(name.find(text=True, recursive=False))
                    item_name.append(prod_name)
                
            if(prod_name!=" "):
                price = listing.find('span', attrs={'class':"s-item__price"})
                prod_price = str(price.find(text=True, recursive=False))
        
                prices.append(prod_price)
        
        #adding all products and prices from this specified 'name_list' search into a list
                all_data.append([name_list[i],prod_name,prod_price])
        
        i+=1
    return all_data




#creates list of all of the data from all urls
all_of_it = ebay_scrape(make_urls(name_list),name_list)


all_of_it
    

    

#creating huge dataframe of all product searches -- check out variable explorer for the dataframe values
dataframe = pd.DataFrame(all_of_it)

#specifying column names for dataframe
dataframe.columns=["Type","Name","Price"]

#set the 'Type' as index of the dataframe -- makes it easier to filter through later on
dataframe.set_index("Type", inplace=True)




#splits up the unique 'Type' into separate data sets
#this part of the program can take up to 5 unique 'Type'
    #we can add more 'elif' statements if necessary 

i = 0 
while i < len(name_list):
    if i == 0:     
        
        dataset1 = dataframe.loc[name_list[0]]
        i+=1
   
    elif i == 1:
        dataset2 = dataframe.loc[name_list[1]]
        i+=1
    
    elif i ==2:
        dataset3 = dataframe.loc[name_list[2]]
        i+=1
    
    elif i ==3:
        dataset4 = dataframe.loc[name_list[3]]
        i+=1
    # only 5 datasets can be created MAX unless we add more 'elif' statements
    elif i ==4:
        dataset5 = dataframe.loc[name_list[4]]
        i+=1
    #this 'else' allows the while loop to end early if we dont have up to 5 values in 'name_list'
    else:
        pass


#Exporting into excel

import xlsxwriter

value = 'Ebay_Practice'

#creating dictionary in order to split up the data into individual sheets
df1 = {name_list[0] :dataset1, name_list[1]:dataset2,name_list[2]: dataset3,name_list[3]: dataset4}





#creating file path below : 

#*************
#WARNING**** MUST UPDATE USER NAME!! MACIO CHANGE THE 'user' TO YOUR COMPUTER NAME!!!
#*************


user = 'Marlena'
writer = pd.ExcelWriter('/Users/'+user+'/Desktop/'+value+'.xlsx',engine='xlsxwriter')


#using dict keys to insert values into new excel document 
for sheet_name in df1.keys():
    
    #sheet_name is refering to 'name_list' values here 
    df1[sheet_name].to_excel(writer,sheet_name=sheet_name, index=True)
writer.save()








