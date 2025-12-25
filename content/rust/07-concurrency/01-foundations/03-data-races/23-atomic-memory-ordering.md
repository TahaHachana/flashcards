## Atomic Memory Ordering

What are memory orderings for atomic operations, and what happens if you use the wrong one?

---

Memory orderings control how atomic operations synchronize with other operations: Relaxed (no ordering guarantees), Acquire/Release (synchronize with matching operations), SeqCst (sequential consistency - strongest guarantees). Wrong ordering can cause subtle bugs where operations appear to happen out of order to different threads, even though no data race occurs. When in doubt, use SeqCst for correctness, optimize later. Atomic operations prevent data races but ordering affects program correctness.

