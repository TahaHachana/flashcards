## Self JOIN Example Structure

In a self-join finding employees and their managers, why do you need table aliases and what would the JOIN condition typically look like?

---

You need aliases (like `e` for employee and `m` for manager) to distinguish between the two instances of the same table. The JOIN condition typically looks like: `e.manager_id = m.employee_id`, connecting each employee's manager_id to the corresponding manager's employee_id in the same table.

