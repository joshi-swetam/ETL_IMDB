# ETL_IMDB

For this project we created relational database for top 250 IMDB TV series and  emmy awards for these series if any for the years 2010-2022.



   ![image](Extraction/IMDB%20image.png)

## Extraction

- For the first source, IMDB <https://www.imdb.com/list/ls008957859/> was scraped to get the data for the title,rank,actors,synopsis, votes, rating etc. The full code for scraping can be found [here](https://github.com/joshi-swetam/ETL_IMDB/blob/main/Extraction/IMDB_Scrape.ipynb) and the resulting dataset can be located [here](https://github.com/joshi-swetam/ETL_IMDB/tree/extract/Extraction/Resources)
- In summary, the csv file was created by looping through all the titles based on the classes and getting the desired output by indexing. 

~~~ 
for each in title_list:
    try:
        
        titles = each.h3.a.get_text()
        title_link = each.h3.a['href'] 
        rank = each.h3.find('span', class_ = 'lister-item-index unbold text-primary').get_text().replace('.', '')
        run_years = each.h3.find('span',class_ = 'lister-item-year text-muted unbold').get_text()
        p_tag = each.find_all('p',class_ = 'text-muted text-small')
        certificate = p_tag[0].find('span', class_= "certificate").get_text().replace('TV-','')
        runtime = p_tag[0].find('span', class_= "runtime").get_text().replace('min','')
        genre = p_tag[0].find('span', class_= "genre").get_text().strip()
        Rating = each.find('span', class_ = 'ipl-rating-star__rating').get_text()
        Actor = p_tag[1].find_all('a')
        Actors = [actor.get_text() for actor in Actor]
        Votes = p_tag[2].find_all('span')[1].get_text().replace(',','')
        Synopsis = each.find_all('p')[1].get_text().strip()
    except :
        pass
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
    print(dict_elements)
~~~


    
- For the csv files of the emmy award winners and nomination across various categories , we used Pandas function `pd.read_html` and got 7 files across the years 2010-2022 which can be loacted [here](https://github.com/joshi-swetam/ETL_IMDB/tree/extract/Extraction/Resources)

## Transformation
For the transformation step following steps were followed: 
-  read data from extracted csv files from [Resources](https://github.com/joshi-swetam/ETL_IMDB/tree/transform/Transformation/Resources) folder
- transform data to generate relational model
- save tranformed data to csv file in [output](https://github.com/joshi-swetam/ETL_IMDB/tree/transform/Transformation/output) folder

## Load

- https://www.quickdatabasediagrams.com/ was used to create [erd](erd) diagram 
![image](Load/erd.png)

- Imdb [schema](https://github.com/joshi-swetam/ETL_IMDB/blob/load/Load/schema.sql) was created using Postgresql and pgADMIN 4 
 - Basic queris such as select titles, rank and rating  and winners yearwise based on  the category from titles and top 250 tables were [performed](https://github.com/joshi-swetam/ETL_IMDB/blob/main/Load/Queries.sql).
