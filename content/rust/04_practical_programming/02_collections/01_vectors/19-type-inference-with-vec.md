## Type Inference with Vec<_>

What does `Vec<_>` mean in `let v: Vec<_> = [1, 2, 3].into();`?

---

The underscore `_` tells Rust to infer the inner type from context. Here it infers `Vec<i32>` from the array. It's a way to specify "this is a Vec but you figure out what's inside."

