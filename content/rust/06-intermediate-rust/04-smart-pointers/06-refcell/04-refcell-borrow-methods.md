## RefCell Borrow Methods

What are the four main methods for borrowing from `RefCell`, and what does each return?

---

**1. `.borrow()` - Immutable borrow:**
```rust
let cell = RefCell::new(vec![1, 2, 3]);
let borrowed = cell.borrow();  // Returns Ref<Vec<i32>>
println!("{:?}", *borrowed);
```
- Returns: `Ref<T>` (acts like `&T`)
- Panics if: Already mutably borrowed

**2. `.borrow_mut()` - Mutable borrow:**
```rust
let cell = RefCell::new(vec![1, 2, 3]);
let mut borrowed = cell.borrow_mut();  // Returns RefMut<Vec<i32>>
borrowed.push(4);
```
- Returns: `RefMut<T>` (acts like `&mut T`)
- Panics if: Already borrowed (mutably or immutably)

**3. `.try_borrow()` - Safe immutable borrow:**
```rust
match cell.try_borrow() {
    Ok(value) => println!("{:?}", *value),
    Err(_) => println!("Already borrowed!"),
}
```
- Returns: `Result<Ref<T>, BorrowError>`
- Doesn't panic, returns error

**4. `.try_borrow_mut()` - Safe mutable borrow:**
```rust
match cell.try_borrow_mut() {
    Ok(mut value) => value.push(5),
    Err(_) => println!("Can't borrow mutably!"),
}
```
- Returns: `Result<RefMut<T>, BorrowMutError>`
- Doesn't panic, returns error

