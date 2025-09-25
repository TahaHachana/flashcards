## Integer Overflow Behavior

How does Rust handle integer overflow in debug and release modes?

---

* Debug mode: Panics at runtime on overflow.
* Release mode: Wraps using two’s complement.

Explicit handling methods:

* `wrapping_*`
* `checked_*`
* `overflowing_*`
* `saturating_*`

