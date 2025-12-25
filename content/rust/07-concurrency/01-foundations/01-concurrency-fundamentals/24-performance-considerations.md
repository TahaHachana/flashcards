## Performance Considerations

What are the key performance considerations when deciding to use concurrency?

---

Consider: (1) Is the work CPU-bound (benefits from parallelism) or I/O-bound (benefits from concurrency)? (2) Does the work justify thread overhead (needs to be substantial)? (3) How many cores are available (no benefit beyond core count for CPU work)? (4) Is there contention for shared resources (locks can serialize execution)? (5) Is the problem naturally parallel or does it require coordination? Measure actual performance rather than assuming concurrency helps.

