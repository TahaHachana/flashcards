## Recursive CTE Common Patterns

What are common use cases for recursive CTEs? Provide examples.

---

Common patterns:

1. Organizational Charts / Employee Hierarchies
   - Start with top-level manager
   - Recursively find all direct and indirect reports
   - Example: CEO → VPs → Managers → Staff

2. Bill of Materials (BOM) / Product Assembly
   - Start with finished product
   - Recursively find all components and sub-components
   - Example: Car → Engine → Pistons → Rings

3. Graph Traversal
   - Start with a node
   - Recursively find all connected nodes
   - Example: Social network connections, road networks

4. File System Hierarchies
   - Start with root directory
   - Recursively find all subdirectories and files
   - Example: / → /home → /home/user → /home/user/documents

5. Category Trees
   - Start with top-level category
   - Recursively find all subcategories
   - Example: Electronics → Computers → Laptops → Gaming Laptops

Common characteristic: Data has parent-child relationships forming a tree or graph structure.

