## Forgetting to Join

What happens if you don't call join() on a spawned thread?

---

If you don't join a thread, you lose its return value and can't detect if it panicked. More critically, if the main thread exits before the spawned thread completes, the spawned thread is killed immediately - it might not finish its work. The thread becomes "detached" and you have no way to wait for it or coordinate with it. Always join threads whose completion you care about.

