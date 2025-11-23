## CTE Versus Views

How do CTEs differ from views, and when should you use each?

---

CTEs (WITH clause):
- Scope: Statement-level (exist only during query)
- Storage: Not stored in database
- Reusability: Only within the defining query
- Security: No separate permissions
- Definition: Inline with query
- Modification: Change query directly

Views (CREATE VIEW):
- Scope: Database-level (persist until dropped)
- Storage: Definition stored in database
- Reusability: Can be used by many queries/users
- Security: Can grant/revoke permissions
- Definition: Separate database object
- Modification: Requires ALTER VIEW or recreate

When to use CTEs:
- Query-specific logic that won't be reused
- Breaking down one complex query
- Exploratory/ad-hoc analysis
- Temporary transformations

When to use views:
- Logic reused across multiple queries
- Standard reports or common data access patterns
- Security/access control (hide sensitive columns)
- Abstraction layer over complex joins
- Stable, well-understood transformations

Example: If 10 different reports need "active customers," create a view. If one report needs temporary intermediate results, use CTEs.

