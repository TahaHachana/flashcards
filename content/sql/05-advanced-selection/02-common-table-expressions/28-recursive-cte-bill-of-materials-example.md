## Recursive CTE Bill Of Materials Example

Explain how a recursive CTE handles a bill of materials (BOM) problem.

---

Problem: Calculate total quantity of each component needed to build a product, accounting for nested assemblies.

Table: parts(part_id, part_name, parent_part_id, quantity)
Represents: Part X contains Y units of Part Z

WITH RECURSIVE bom AS (
  -- Anchor: Start with finished product
  SELECT 
    part_id, part_name, parent_part_id,
    quantity,
    1 as level
  FROM parts
  WHERE part_id = 1001  -- Finished product
  
  UNION ALL
  
  -- Recursive: Find components of parts found so far
  SELECT 
    p.part_id, p.part_name, p.parent_part_id,
    p.quantity * bom.quantity,  -- Multiply quantities through tree
    bom.level + 1
  FROM parts p
  JOIN bom ON p.parent_part_id = bom.part_id
)
SELECT part_name, quantity, level
FROM bom
ORDER BY level, part_name;

How it works:
1. Start with finished product (e.g., "Bicycle")
2. Find direct components (e.g., "Frame", "Wheel" x2)
3. Find components of those (e.g., Frame needs "Tube" x3)
4. Continue until no more components
5. Multiply quantities through the hierarchy

Result: Complete list of every component needed with correct quantities.

Why recursive CTE: Alternative would require knowing depth ahead of time or writing complex procedural code.

