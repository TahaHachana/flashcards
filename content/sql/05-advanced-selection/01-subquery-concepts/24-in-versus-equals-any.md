## IN Versus = ANY

What is the relationship between the IN operator and = ANY?

---

They are completely equivalent - they mean exactly the same thing!

These queries are identical:
WHERE city IN ('Paris', 'London', 'Rome')
WHERE city = ANY ('Paris', 'London', 'Rome')

Both check: Is the value equal to at least one value in the set?

By convention, IN is more commonly used because it's more readable and familiar to most SQL developers.

