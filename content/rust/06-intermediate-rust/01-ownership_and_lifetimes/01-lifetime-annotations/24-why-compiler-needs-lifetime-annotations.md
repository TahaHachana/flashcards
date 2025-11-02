## Why Compiler Needs Lifetime Annotations

Why can't the Rust compiler always figure out lifetimes automatically without annotations?

---

When a function returns a reference, the compiler needs to know which input(s) it comes from to verify the reference remains valid. With multiple reference inputs, there's ambiguity—the compiler can't determine if the output relates to the first input, second input, or both. Lifetime annotations resolve this ambiguity by explicitly specifying the relationship. (Note: in many simple cases, "lifetime elision" rules DO allow the compiler to infer lifetimes automatically.)

