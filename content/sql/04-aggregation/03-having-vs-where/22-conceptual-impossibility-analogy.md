## Conceptual Impossibility Analogy

Use an analogy to explain why WHERE can't filter on aggregate values.

---

It's like asking a teacher to "exclude students who failed the test" before the test has been graded. The information needed to make that decision (test scores) doesn't exist yet. Similarly, WHERE asks SQL to filter on aggregate values (like COUNT) before those values have been calculated. The aggregates are "graded" during GROUP BY, which happens after WHERE.

