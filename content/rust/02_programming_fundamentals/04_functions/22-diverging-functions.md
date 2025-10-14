## Diverging Functions

What is a diverging function and how do you declare it?

---

A function that never returns, using the ! (never) type. Used for functions that panic or loop forever.

```rust
fn exit_program() -> ! {
    panic!("Terminated!");
}
fn infinite_loop() -> ! {
    loop { }
}
```

