## Natural vs Surrogate Keys

What's the difference between natural keys and surrogate keys? When should you use each?

---

Natural key: Uses real data
- Examples: email, ISBN, country code ('US', 'CA')
- Pro: Has meaning
- Con: Can change (people change emails)

Surrogate key: Arbitrary identifier
- Examples: customer_id (1, 2, 3...)
- Pro: Never needs to change
- Con: No inherent meaning

When to use:
- Surrogate: Most tables (customer_id, order_id, product_id)
- Natural: Only when guaranteed stable (country codes, ISBN)

Best practice: Default to surrogate keys unless you have a stable natural key.

