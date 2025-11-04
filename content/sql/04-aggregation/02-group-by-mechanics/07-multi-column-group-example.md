## Multi Column Group Example

Given `GROUP BY actor_id, rating`, describe what groups are created and give examples.

---

Groups are created for each unique combination of actor and rating. Examples: (actor_id=1, rating='G'), (actor_id=1, rating='PG'), (actor_id=1, rating='R'), (actor_id=2, rating='G'), etc. If there are 200 actors and 5 ratings, you could have up to 1000 groups (though likely fewer since not every actor appears in every rating).

