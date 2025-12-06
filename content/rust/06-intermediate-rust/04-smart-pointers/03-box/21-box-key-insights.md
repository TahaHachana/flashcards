## Box Key Insights

What are the seven key insights about `Box<T>`?

---

**1. Box is indirection:** Moves data to heap, gives you a pointer

**2. Enables recursive types:** Provides known size for self-referential structures

**3. Enables trait objects:** Allows returning different types through same interface

**4. Automatic cleanup:** Drop ensures no memory leaks

**5. Single ownership:** Box cannot be shared (use Rc/Arc for that)

**6. Zero runtime overhead:** Besides allocation, no ongoing cost like reference counting

**7. Use judiciously:** Stack is faster; use Box when you need its specific benefits

**Mental model:** Box is Rust's way of saying "put this on the heap" while maintaining ownership and safety guarantees.

**Bottom line:** Box is simple but powerful - it's the foundation for heap allocation in safe Rust.

