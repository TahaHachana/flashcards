## Array Insert and Delete Complexity

What is the time complexity of inserting or deleting an element in the middle of an array, and why?

---

Time complexity: O(n) for both insertion and deletion in the middle

Insert operation:
1. Find insertion position: O(1)
2. Shift elements to make space: O(n)
3. Insert new element: O(1)
Total: O(n)

Delete operation:
1. Find element position: O(1) if by index, O(n) if by value
2. Delete element: O(1)
3. Shift elements to fill gap: O(n)
Total: O(n)

Reason: Must maintain sequential order by shifting up to n elements.

