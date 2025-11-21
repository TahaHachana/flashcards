## Fn Trait Hierarchy

Explain the hierarchy relationship between `FnOnce`, `FnMut`, and `Fn` traits. Which traits does each implement?

---

The three traits form a hierarchy through supertraits:

```
FnOnce (base - all closures implement this)
   ↑
FnMut (also implements FnOnce)
   ↑
Fn (implements FnMut and FnOnce)
```

**What each trait implements:**
- `FnOnce`: Only itself (base trait)
- `FnMut`: Both `FnMut` and `FnOnce`
- `Fn`: All three: `Fn`, `FnMut`, and `FnOnce`

**Practical implication:**
- A function requiring `FnOnce` accepts ANY closure
- A function requiring `FnMut` accepts `FnMut` or `Fn` closures
- A function requiring `Fn` only accepts `Fn` closures (most restrictive)

This means `Fn` closures are the most flexible - they can be used anywhere.

