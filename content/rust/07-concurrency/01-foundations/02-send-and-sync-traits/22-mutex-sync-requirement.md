## Mutex Sync Requirement

Why is Mutex<T> Sync when T is Send (but T doesn't need to be Sync)?

---

Mutex<T> is Sync because the lock ensures synchronized access - only one thread can access T at a time through the MutexGuard. T needs to be Send because when you lock the mutex, you're effectively transferring access to T to the locking thread (though not ownership). T doesn't need to be Sync because the Mutex itself provides the synchronization - the inner T is never simultaneously accessed.

