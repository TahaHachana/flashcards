## Test Output Interpretation

How do you interpret integration test output?

---

Output shows each test file separately:

```
running 2 tests (src/lib.rs)
test tests::unit_test_1 ... ok
test tests::unit_test_2 ... ok

running 3 tests (integration_test)
test test_api ... ok
test test_integration ... ok
test test_error ... ok

running 1 test (workflow_test)
test test_full_workflow ... ok

test result: ok. 6 passed; 0 failed
```

Reading the output:
- Unit tests show module path (`src/lib.rs`)
- Integration tests show filename (`integration_test`)
- Each integration file is a separate test run
- Total summary at the end

Failed integration tests show:
- Which test file failed
- Which specific test within that file
- Full error details and assertion failures

