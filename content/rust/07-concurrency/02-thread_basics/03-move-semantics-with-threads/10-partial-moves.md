## Partial Moves

Can a move closure move some variables and copy others?

---

Yes. The move keyword moves all captured variables, but Copy types are copied (not moved) and remain accessible. Example: let x = 42; let s = String::from("hi"); thread::spawn(move || { /* x copied, s moved */ }); println!("{}", x); // OK - x is Copy; println!("{}", s); // Error - s was moved. Each variable's behavior depends on whether it implements Copy.

