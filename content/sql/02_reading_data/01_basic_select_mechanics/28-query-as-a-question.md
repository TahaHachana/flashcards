## Query As a Question

What does it mean to think of a SELECT query as "asking a question"?

---

Mental model: You ask the database a question, it answers with a result set.

Examples:
```sql
SELECT name FROM customers WHERE age >= 21;
```
Question: "Who are the customers aged 21 or older?"
Answer: Table of names

```sql
SELECT product, price FROM products WHERE price < 50;
```
Question: "What products cost less than $50?"
Answer: Table of products and prices

Why this helps:
1. Makes query intent clear
2. Helps you write the right SQL
3. Result set is the "answer"
4. You're not commanding, you're inquiring

The database is an expert that knows how to find the answer efficiently.

