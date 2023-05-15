-- select titles, rank and rating  and winners yearwise based on  the category from titles and top 250 tables

select 
t.title , i.rank, i.rating ,n.year,a.award, c.category,ac.actor
from imdb_top_250 as i
join title as t
on i.title_id = t.title_id 
join nomination as n 
on n.title_id = t.title_id
join award as a 
on n.award_id = a.award_id 
join actor as ac 
on ac.actor_id = n.actor_id
join category as c
on c.category_id = n.category_id
where year = 2020 and n.winner = True and c.category = 'Drama';


-- Series winner across years 

select 
t.title,n.year, ac.actor , a.award
from imdb_top_250 as i
join title as t
on i.title_id = t.title_id 
join nomination as n 
on n.title_id = t.title_id
join actor as ac 
on ac.actor_id = n.actor_id
join award as a 
on n.award_id = a.award_id 
where t.title = 'Breaking Bad' and n.winner = True ;



