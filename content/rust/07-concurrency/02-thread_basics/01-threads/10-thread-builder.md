## Thread Builder

What is thread::Builder and what configuration options does it provide?

---

thread::Builder provides more control over thread creation than spawn. It allows you to: (1) Set thread name with name() for debugging and logging, (2) Set stack size with stack_size() (default is ~2MB on most platforms). You call spawn() on the builder to create the thread. Builder is useful when you need named threads for profiling or need custom stack sizes for deep recursion or memory constraints.

