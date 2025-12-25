## Message Passing Send Requirement

Why do channels (mpsc::channel) require sent data to be Send?

---

Channels transfer ownership of data from the sending thread to the receiving thread. The data must be Send because it's being moved across thread boundaries. The sender gives up ownership and the receiver gains it. If the data weren't Send, this transfer could violate thread safety (like trying to send Rc between threads, which could corrupt its non-atomic reference count).

