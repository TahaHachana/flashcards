## Send Sync Library Design

When designing a library with public types, why should you care about Send and Sync?

---

Send and Sync determine whether users can use your types in concurrent code. If your type isn't Send/Sync, users can't share it between threads, limiting your library's applicability. Public API types should ensure their fields are Send/Sync unless there's a specific reason not to be. These traits communicate thread safety guarantees to users at compile time, becoming part of your API contract.

