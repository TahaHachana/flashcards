## Elision Is Not Magic

What is lifetime elision NOT?

---

Lifetime elision is NOT:
- Magic: The compiler follows mechanical rules, not AI inference
- Always applicable: Some signatures still need explicit annotations
- A different type of lifetime: Elided lifetimes follow the same rules as explicit ones
- Optional: When elision rules apply, you must omit annotations (or they must match what elision would infer)

