## Cascade Options

What are the three main ON DELETE options for foreign keys? When would you use each?

---

1. ON DELETE RESTRICT (default)
   - Prevent deletion if children exist
   - Must delete children first
   - Use: When children should be handled explicitly
   ```sql
   DELETE FROM customers WHERE customer_id = 1;  -- ERROR if has orders
   ```

2. ON DELETE CASCADE
   - Automatically delete children when parent deleted
   - Use: When children can't exist without parent
   ```sql
   DELETE FROM customers WHERE customer_id = 1;  -- Also deletes all orders
   ```

3. ON DELETE SET NULL
   - Set foreign key to NULL when parent deleted
   - Use: When children can exist without parent
   ```sql
   DELETE FROM customers WHERE customer_id = 1;  -- Orders remain, customer_id → NULL
   ```

Choose based on business rules. RESTRICT is safest.

