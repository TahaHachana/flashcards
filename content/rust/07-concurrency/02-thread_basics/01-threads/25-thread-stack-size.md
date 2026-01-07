## Thread Stack Size

What is the default thread stack size, when might you need to change it, and how?

---

Default is ~2MB on most platforms. Change it with thread::Builder::new().stack_size(bytes). Increase for: (1) Deep recursion that would overflow, (2) Large stack-allocated data structures. Decrease for: (1) Memory-constrained environments, (2) Many threads where total memory matters. Stack overflow causes panic. Note: stack size is per-thread, so 100 threads with 4MB stacks = 400MB just for stacks.

