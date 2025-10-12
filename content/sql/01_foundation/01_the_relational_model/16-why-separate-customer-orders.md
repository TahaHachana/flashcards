## Why Separate Customer and Orders Tables

Explain why customer information and order information should be in separate tables rather than combined.

---

Reasons to separate:

1. Eliminates redundancy: Customer name/email stored once, not in every order
2. Prevents inconsistency: Update customer info in one place
3. Follows normalization: Each table represents one type of entity
4. Maintains independence: Can update customers without touching orders
5. Enables flexibility: Customer can exist without orders; can query orders or customers independently

Connection: customer_id (foreign key) links them together

