## Move Keyword Requirement

Why is the move keyword required when capturing variables in thread closures?

---

The move keyword transfers ownership of captured variables into the thread's closure. Without it, the closure would borrow variables, but the compiler can't guarantee those borrows remain valid - the thread might outlive the scope where the variables were created. move ensures the thread owns its data, preventing dangling references and enabling the thread to run independently of its parent scope.

