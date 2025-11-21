## Library vs Application Code

Should you use different dispatch strategies for library code vs application code?

---

**Library code** - Prefer static dispatch (generics):
```rust
// Library API - users get zero-cost abstraction
pub fn map<T, U, F>(iter: T, f: F) -> Map<T, F>
where
    T: Iterator,
    F: FnMut(T::Item) -> U,
{
    // Maximum flexibility and performance for users
}
```

**Application code** - Prefer dynamic dispatch initially:
```rust
// Application - use trait objects for simplicity
fn handle_requests(handlers: Vec<Box<dyn RequestHandler>>) {
    for handler in handlers {
        handler.handle();
    }
}
```

**Rationale**:
- Libraries: Users can't change internals, need maximum performance
- Applications: You can profile and optimize specific bottlenecks
- Start simple, optimize when needed

