## If Let Usage

When is `if let` preferred over a full `match`?

---

When only one pattern matters and all other cases can be ignored.
It avoids writing a `_` catch-all arm.

