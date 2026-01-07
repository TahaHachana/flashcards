## Resume Unwind

What is panic::resume_unwind and when would you use it?

---

resume_unwind takes a panic payload and continues the panic, propagating it upward. Use when you catch a panic with catch_unwind but want to: (1) Inspect or log the panic before propagating, (2) Add context to the panic, (3) Conditionally re-panic based on the payload type. Example: catch panic, log details to monitoring system, then resume_unwind to propagate the panic to the caller.

