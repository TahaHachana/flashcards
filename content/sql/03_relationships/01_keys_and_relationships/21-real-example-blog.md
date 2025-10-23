## Real Example Blog System

Design a blog system with Users, Posts, and Tags. Identify the relationships and where foreign keys go.

---

Entities and relationships:
- Users write Posts: one-to-many
- Posts have Tags: many-to-many
- Tags on Posts: many-to-many

Structure:
```
Users:
user_id (PK) | username

Posts:
post_id (PK) | user_id (FK) | title | content

Tags:
tag_id (PK) | tag_name

PostTags (junction):
post_id (FK) | tag_id (FK)
```

Relationships:
- Users → Posts: FK in Posts (one user, many posts)
- Posts ↔ Tags: Junction table PostTags (posts have many tags, tags on many posts)

Why this design:
- User info stored once
- Can find all posts by a user
- Can find all tags on a post
- Can find all posts with a tag

