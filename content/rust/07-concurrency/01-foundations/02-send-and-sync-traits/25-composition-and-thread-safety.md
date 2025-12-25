## Composition and Thread Safety

If you have a struct with fields Arc<Mutex<Vec<String>>>, is this struct Send and Sync? Why?

---

Yes, this struct is both Send and Sync. Breaking it down: String is Send+Sync, Vec<String> is Send+Sync (because String is), Mutex<Vec<String>> is Send+Sync (because Vec<String> is Send), and Arc<Mutex<Vec<String>>> is Send+Sync (because Mutex<Vec<String>> is). Since all fields are Send+Sync, the struct is automatically Send+Sync through composition.

