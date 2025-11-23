## What Is A Common Table Expression?

What is a Common Table Expression (CTE), and what are its key characteristics?

---

A CTE is a named temporary result set defined at the beginning of a query using the WITH clause.

Key characteristics:
- Defined using WITH clause at the top of a query
- Must have a name (alias)
- Acts like a temporary view that exists only for query duration (statement scope)
- Can be referenced by name anywhere in the subsequent query
- Multiple CTEs can be defined in one WITH clause (comma-separated)
- Later CTEs can reference earlier CTEs defined above them

Mental model: CTEs are named intermediate results that serve as building blocks. Instead of one giant nested query, you break it into logical, named steps.

