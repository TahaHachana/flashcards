## Ownership Rules and Data Races

How do Rust's core ownership rules (one owner, one mutable or many immutable borrows) naturally prevent data races?

---

Each value has one owner, so only one thread can own data at a time (prevents shared access). The borrowing rule "one mutable or many immutable" prevents having a mutable reference in one thread while another thread accesses the data. These rules prevent the conditions for data races: if only one thread owns the data, or if all accesses are reads, data races are impossible. The same rules that prevent memory errors also prevent data races.

