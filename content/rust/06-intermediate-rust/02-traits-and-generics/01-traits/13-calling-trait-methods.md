## Calling Trait Methods Two Ways

What are the two ways to call a trait method on a value?

---

1. **Method syntax** (common):
```rust
value.method();
```

2. **Fully qualified syntax** (explicit):
```rust
TraitName::method(&value);
```

Both do the same thing. Fully qualified syntax is useful when there are naming conflicts or for clarity.

Example:
```rust
let dog = Dog;
dog.make_sound();            // Method syntax
Animal::make_sound(&dog);    // Fully qualified
```

