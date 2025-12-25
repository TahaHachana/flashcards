## Doc Test Crate Level Documentation

Where and how do you write crate-level documentation?

---

In `lib.rs` or `main.rs` at the very top:

```rust
//! # My Awesome Crate
//!
//! This crate provides tools for data processing.
//!
//! ## Quick Start
//!
//! ```
//! use my_crate::Processor;
//!
//! let processor = Processor::new();
//! let result = processor.process("input");
//! assert_eq!(result, "processed: input");
//! ```
//!
//! ## Features
//!
//! - Fast processing
//! - Memory efficient
//! - Easy to use

pub struct Processor { /* ... */ }
```

Crate-level docs appear on:
- Main documentation page
- crates.io page
- README context

Should include:
- What the crate does
- Quick start example
- Key features
- Links to important items

First impression for users!

