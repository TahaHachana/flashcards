## Always Heap Types

Which Rust types always store their actual data on the heap?

---

String, Vec<T>, Box<T>, HashMap<K,V>, Rc<T>, and Arc<T>. These types store metadata/pointers on the stack but their actual data content lives on the heap.

