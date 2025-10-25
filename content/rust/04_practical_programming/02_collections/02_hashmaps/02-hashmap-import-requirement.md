## HashMap Import Requirement

Why does HashMap require `use std::collections::HashMap;` while Vec doesn't need an import?

---

HashMap is not in the prelude (the set of items Rust automatically imports into every program), while Vec is. You must explicitly import HashMap with `use std::collections::HashMap;` at the top of your file.

