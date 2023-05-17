select
t.title, 'Best Lead Actor/Actress' as awards, count(a.award) AS numOfAwards
from imdb_top_250 as i
join title as t
on i.title_id = t.title_id 
join nomination as n 
on n.title_id = t.title_id
join actor as ac 
on ac.actor_id = n.actor_id
join award as a 
on n.award_id = a.award_id 
where a.award like 'Best Lead Actor%'
and n.winner = True 
GROUP BY t.title, awards
ORDER BY numOfAwards DESC
LIMIT 10;