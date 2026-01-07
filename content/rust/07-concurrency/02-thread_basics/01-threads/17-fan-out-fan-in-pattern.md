## Fan Out Fan In Pattern

What is the fan-out/fan-in pattern in concurrent programming?

---

Fan-out: distribute work to multiple threads (spawn multiple workers with different inputs). Fan-in: collect results from all threads back into one place. Typically use channels where each thread sends its result, then collect all results from the channel. Pattern enables parallel processing where each worker does independent work, then results are aggregated. Example: spawn 10 threads doing different computations, collect all 10 results.

