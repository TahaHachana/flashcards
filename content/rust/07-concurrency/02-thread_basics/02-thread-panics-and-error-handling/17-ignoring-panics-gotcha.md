## Ignoring Panics Gotcha

Why is let _ = handle.join() dangerous, and what should you do instead?

---

Using let _ = handle.join() silently discards the Result, hiding thread panics. You won't know if the thread failed, lost its work, or produced incorrect state. Always handle the Result: use match, unwrap/expect with meaningful messages, or ? to propagate. In production, log errors and take appropriate action (retry, alert, graceful degradation). Silent failures are the worst kind of failures.

