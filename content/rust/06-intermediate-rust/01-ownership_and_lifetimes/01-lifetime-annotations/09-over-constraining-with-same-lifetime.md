## Over-Constraining with Same Lifetime

What's wrong with using the same lifetime for all parameters when not necessary?
```rust
fn process<'a>(input: &'a str, buffer: &'a mut String) -> &'a str {
    buffer.push_str(input);
    input
}
```

---

This is too restrictive because it forces `buffer` to live as long as the return value, even though the return is only tied to `input`. Use independent lifetimes when parameters aren't related:
```rust
fn process<'a, 'b>(input: &'a str, buffer: &'b mut String) -> &'a str {
    buffer.push_str(input);
    input
}
```

