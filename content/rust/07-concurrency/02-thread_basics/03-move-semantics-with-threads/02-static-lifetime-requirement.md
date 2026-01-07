## Static Lifetime Requirement

Why do threads require 'static lifetime or ownership of their data?

---

Threads can outlive the scope that created them - they might run for the entire program lifetime. If a thread borrowed non-'static data, that data could be dropped while the thread still references it, causing use-after-free. The 'static requirement ensures data lives as long as needed. The move keyword satisfies this by transferring ownership - the thread owns the data, so it lives as long as the thread needs it.

