## Drop is Automatic

Do you need to manually call drop in most Rust code?

---

No. The compiler automatically inserts drop code at scope boundaries. Manual drop with std::mem::drop is rare and used only for early resource release.

