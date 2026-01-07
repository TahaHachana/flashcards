## Testing and Catch Unwind

How does Rust's test framework use catch_unwind?

---

The test framework wraps each test in catch_unwind so one test's panic doesn't prevent other tests from running. Each test runs in isolation - panics are caught, reported as failures, and testing continues. The #[should_panic] attribute expects a panic and fails if it doesn't occur. This demonstrates catch_unwind's use for isolating failures in a controlled environment.

