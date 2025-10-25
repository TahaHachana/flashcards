## Borrow Checker Is Conservative

Why does the borrow checker sometimes reject safe code?

---

It's conservative - rejects code if it can't prove it's safe. This is intentional to maintain safety guarantees. Better to reject safe code than allow unsafe code.

