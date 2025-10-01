## Ownership Summary

Summarize the key points of ownership in Rust.

---

* Each value has one owner.
* Only one owner exists at a time.
* Values are dropped when the owner goes out of scope.
* Moving transfers ownership, invalidating the original.
* Copy types are duplicated instead of moved.
* Cleanup is automatic via the `Drop` trait.
* `String` illustrates ownership with heap-allocated text.

