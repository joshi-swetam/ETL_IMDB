from splinter import Browser
from bs4 import BeautifulSoup as soup
import time
import pandas as pd
import os
# Set up Splinter
browser = Browser('chrome')


url = 'https://www.imdb.com/list/ls063868333/'
browser.visit(url)
html = browser.html
imdb_soup = soup(html , 'html.parser')
title_list = imdb_soup.find_all('div',class_ = 'lister-item-content')
all_details_list = []
for each in title_list:
    titles = each.h3.a['href']
    title_link = each.h3.a.get_text()
    rank = each.h3.find('span', class_ = 'lister-item-index unbold text-primary').get_text().replace('.', '')
    run_years = each.h3.find('span',class_ = 'lister-item-year text-muted unbold').get_text()
    p_tag = each.find_all('p',class_ = 'text-muted text-small')
    certificate = p_tag[0].find('span', class_= "certificate").get_text().replace('TV-','')
    runtime = p_tag[0].find('span', class_= "runtime").get_text().replace('min',' ')
    genre = p_tag[0].find('span', class_= "genre").get_text().strip()
    Rating = each.find('span', class_ = 'ipl-rating-star__rating').get_text()
    Actor = p_tag[1].find_all('a')
    Actors = [actor.get_text() for actor in Actor]
    Votes = p_tag[2].find_all('span')[1].get_text().replace(',','')
    Synopsis = each.find_all('p')[1].get_text().strip()
    dict_elements = {'Title' : titles,
                    'url' : title_link,
                    'Rank' : rank,
                    'Years of running' : run_years,
                    'Certificate' : certificate,
                    'Run time in minutes' : runtime,
                    'Genre' : genre,
                    'Rating' : Rating,
                    'Actors' : Actors,
                    'Votes' : Votes,
                    'Synopsis' : Synopsis}                        
    # Add the dictionary to the list
    all_details_list.append(dict_elements)    
Shows_df = pd.DataFrame(all_details_list)   
Shows_df
os.makedirs('ETL_practice/Resources', exist_ok=True)  
IMDB_df = Shows_df.to_csv('ETL_practice/Resources/Top 100 TV Series_Netflix.csv')      
browser.quit()
