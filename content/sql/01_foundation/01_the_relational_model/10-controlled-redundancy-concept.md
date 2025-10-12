## Controlled Redundancy Concept

What is "controlled redundancy" in relational databases, and why is it necessary?

---

Controlled redundancy means foreign keys are the ONLY data that is intentionally repeated across tables.

Why it's necessary: Foreign keys are what create relationships between tables.

Example:
- Customer name appears ONCE in Customers table
- But customer_id appears in both Customers and Orders tables
- The customer_id is controlled redundancy that links the tables

This is the foundation of how normalized tables stay connected.

