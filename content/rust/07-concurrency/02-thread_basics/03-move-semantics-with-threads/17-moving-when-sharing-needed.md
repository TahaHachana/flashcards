## Moving When Sharing Needed

What's wrong with this: `thread::spawn(move || use data); thread::spawn(move || use data);`?

---

Error: "value moved" or "use of moved value". You can only move data once - after the first spawn moves it, data is gone and unavailable for the second spawn. Fix: use Arc. Pattern: let data = Arc::new(data); let d1 = Arc::clone(&data); spawn(move || use d1); let d2 = Arc::clone(&data); spawn(move || use d2);. Each thread gets its own Arc (moved in) pointing to shared data.

