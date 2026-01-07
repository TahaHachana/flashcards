## Scoped Borrowing Rules

Do scoped threads allow you to bypass Rust's borrowing rules?

---

No. Scoped threads allow borrowing (instead of requiring move), but still enforce all borrowing rules: one mutable XOR many immutable borrows. You can't have one thread mutably borrowing while another immutably borrows, even in the same scope. Scoped threads relax the lifetime requirement (allow non-'static) but not the exclusivity requirement (one mutable or many immutable). Borrowing rules always apply.

