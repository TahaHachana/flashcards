## What Is Lifetime Elision?

What is lifetime elision in Rust, and why does it exist?

---

Lifetime elision is a set of rules the Rust compiler uses to automatically infer lifetime annotations in common patterns, allowing you to omit them from your code. It exists because early Rust required explicit lifetime annotations everywhere, which was verbose and tedious. The Rust team noticed most lifetime annotations followed predictable patterns, so they added elision rules to let the compiler infer them automatically. It's purely syntactic sugar—the compiled code is identical.

