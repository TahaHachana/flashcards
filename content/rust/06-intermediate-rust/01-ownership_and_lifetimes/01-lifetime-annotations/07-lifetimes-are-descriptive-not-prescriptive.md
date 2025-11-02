## Lifetimes Are Descriptive Not Prescriptive

Do lifetime annotations change how long data actually lives?

---

No. Lifetimes are descriptive, not prescriptive. They describe existing relationships between references but don't change how long data lives. Data lifetime is determined by scope and ownership—lifetime annotations just help the compiler verify that references remain valid.

