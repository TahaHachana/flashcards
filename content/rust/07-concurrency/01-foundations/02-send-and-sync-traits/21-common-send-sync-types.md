## Common Send Sync Types

List common types that are both Send and Sync.

---

Types that are both Send and Sync: (1) All primitive types (i32, f64, bool, char), (2) String and &str, (3) Vec<T>, HashMap<K,V> when T, K, V are Send+Sync, (4) Box<T>, Arc<T> when T is Send+Sync, (5) Mutex<T>, RwLock<T> when T is Send, (6) Most standard library types. These are the building blocks of safe concurrent programs.

