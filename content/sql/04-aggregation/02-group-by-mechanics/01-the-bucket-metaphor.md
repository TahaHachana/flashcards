## The Bucket Metaphor

What does GROUP BY do conceptually, using the bucket metaphor?

---

GROUP BY creates separate buckets where each bucket contains rows that share something in common. Without GROUP BY, all rows go into one big bucket (implicit grouping). With GROUP BY, rows are sorted into separate buckets based on column values - each unique value or combination gets its own bucket. Aggregate functions then calculate independently for each bucket, producing one result row per bucket.

