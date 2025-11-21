## Vtable Lookup Process

Describe the step-by-step process of a method call through a trait object.

---

```rust
let animal: &dyn Animal = &dog;
animal.make_sound();
```

**Step-by-step**:
1. **Read trait object fat pointer** (2 pointers: data + vtable)
2. **Follow vtable pointer** to vtable in memory
3. **Index into vtable** to find `make_sound` function pointer
4. **Read function pointer** from vtable
5. **Call function** with data pointer as argument
6. **Function executes** Dog's implementation

**Cost**: Steps 2-4 add ~2-5 nanoseconds
**Compare to static dispatch**: Direct call to known function (can be inlined)

The extra memory accesses (vtable lookup) are why dynamic dispatch is slightly slower.

