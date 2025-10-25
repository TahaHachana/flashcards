## Slices Are References

How do slices relate to references?

---

Slices are references that follow borrowing rules. They don't own data, can be immutable (&[T]) or mutable (&mut [T]), can't outlive data, and same mutability exclusivity rules apply.

