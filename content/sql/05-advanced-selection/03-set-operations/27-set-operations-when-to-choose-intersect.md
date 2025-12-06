## Set Operations When To Choose INTERSECT

When should you use INTERSECT, and what questions does it answer?

---

Use INTERSECT when you need to answer: "What's in both A AND B?"

Ideal use cases:

1. Finding commonality between datasets
   - Which customers are also employees?
   - Which products sold in both regions?

2. Validating data appears in multiple places
   - Verify records exist in both source and destination
   - Check synchronization between systems

3. Finding dual roles or relationships
   - People who are both buyers and sellers
   - Products that are both inputs and outputs

4. Set-based validation
   - Does this list match that list?
   - Are these two queries equivalent?

Example scenarios:

Business: "Find customers who bought products from both categories"
SELECT customer_id FROM purchases WHERE category = 'Electronics'
INTERSECT
SELECT customer_id FROM purchases WHERE category = 'Clothing';

Validation: "Which IDs exist in both our system and partner system?"
SELECT id FROM our_records
INTERSECT
SELECT external_id FROM partner_records;

Key advantage: Makes "commonality" intent explicit and clear.

Alternative: INNER JOIN with DISTINCT can achieve similar results but INTERSECT is more direct for pure set membership questions.

