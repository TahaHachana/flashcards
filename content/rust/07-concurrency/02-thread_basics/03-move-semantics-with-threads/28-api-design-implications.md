## API Design Implications

What should library designers consider about move semantics and threads?

---

Consider: (1) Should types be Send/Sync? (2) Should APIs take ownership or references? (3) Should you provide Arc-wrapped versions? (4) How will users share data? Good practices: make types Send/Sync unless there's a reason not to, document thread-safety clearly, consider providing Arc::new helpers, think about whether users will need to share instances. API design communicates ownership and sharing expectations.

