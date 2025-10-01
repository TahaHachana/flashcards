## Integer Overflow

How does Rust handle integer overflow in debug vs release modes?

---

* **Debug mode**: Program panics on overflow.
* **Release mode**: Value wraps using two’s complement.
* Methods for control: `wrapping_*`, `checked_*`, `overflowing_*`, `saturating_*`.

