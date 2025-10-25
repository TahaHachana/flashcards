## HashMap vs BTreeMap Ordering

When should you use BTreeMap instead of HashMap?

---

Use BTreeMap when you need keys in sorted order. 

**HashMap**: Unordered, O(1) average access, faster for most operations
**BTreeMap**: Sorted by key, O(log n) access, guarantees iteration in key order

APIs are nearly identical, making switching easy.

