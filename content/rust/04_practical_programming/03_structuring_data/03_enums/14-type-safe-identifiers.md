## Type-Safe Identifiers with Enums

How can you use single-variant enums to create type-safe identifiers?

---

Wrap primitive types in distinct enum types:

```rust
enum UserId { Id(u64) }
enum ProductId { Id(u64) }
enum OrderId { Id(u64) }

fn get_user(id: UserId) -> User { /* ... */ }
fn get_product(id: ProductId) -> Product { /* ... */ }

let user_id = UserId::Id(42);
let product_id = ProductId::Id(42);

get_user(user_id);           // OK
// get_user(product_id);     // ERROR: type mismatch!
```

**Benefits**:
- Prevents mixing up IDs
- Compile-time type safety
- Self-documenting code
- Zero runtime cost (compiler optimizes away the wrapper)

Even though all IDs are u64 internally, the type system treats them as different types.

