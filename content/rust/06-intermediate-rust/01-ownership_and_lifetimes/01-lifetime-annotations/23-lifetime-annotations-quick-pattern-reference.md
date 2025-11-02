## Lifetime Annotations Quick Pattern Reference

What does each of these signature patterns express?
1. `fn f<'a>(x: &'a T) -> &'a T`
2. `fn f<'a, 'b>(x: &'a T, y: &'b U) -> &'a T`
3. `fn f<'a>(x: &'a T)`
4. `where 'b: 'a`

---

1. Single lifetime: output lifetime tied to input
2. Multiple lifetimes: output tied to one input only (x)
3. No output reference: input used temporarily (often elided)
4. Lifetime bound: `'b` outlives `'a` (lives at least as long)

