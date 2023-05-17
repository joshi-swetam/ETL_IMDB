select
net.Network, count(t.title) AS numOfShows
from imdb_top_250 as i
join title as t
on i.title_id = t.title_id 
join nomination as n 
on n.title_id = t.title_id
join category as c
on n.category_id = c.category_id
join award as a 
on n.award_id = a.award_id 
join network as net
on net.network_id = n.network_id
where a.award like 'Best Lead Actor%'
and n.winner = True
Group by net.Network
ORDER BY numOfShows DESC
LIMIT 10;