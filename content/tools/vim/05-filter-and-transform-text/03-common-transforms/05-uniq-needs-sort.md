## Why uniq Usually Follows sort

Why is `uniq` almost always preceded by `sort`?

---

`uniq` only removes ADJACENT duplicate lines. Unsorted input leaves non-neighboring duplicates intact, so you sort first to bring duplicates together.

