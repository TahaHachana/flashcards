## Builder Pattern with Move

How does move semantics work with configuration structs passed to threads?

---

Create a config struct, then move the entire struct into the thread. Pattern: let config = Config { name, iterations }; thread::spawn(move || { use config.name, config.iterations });. The thread owns the config, accessing its fields as needed. This is cleaner than moving individual fields and allows grouping related configuration. The struct is moved as a single unit.

