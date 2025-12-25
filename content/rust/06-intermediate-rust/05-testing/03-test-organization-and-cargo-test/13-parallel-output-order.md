## Output Order in Parallel Tests

What problem occurs with test output in parallel execution and how do you fix it?

---

Problem: Output from parallel tests is interleaved and unreadable:

```bash
$ cargo test -- --nocapture
Test 1: Step A
Test 2: Step A
Test 1: Step B
Test 3: Step A
Test 2: Step B
Test 1: Step C
```

Solution: Run sequentially for readable output:

```bash
$ cargo test -- --test-threads=1 --nocapture
Test 1: Step A
Test 1: Step B
Test 1: Step C
Test 2: Step A
Test 2: Step B
Test 3: Step A
```

Use sequential execution when:
- Debugging with print statements
- Need to see execution flow
- Reading test output is important

Trade-off: Slower execution but clearer output.

