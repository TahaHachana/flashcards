## The --nocapture Flag

What does `--nocapture` do and why do you need the double dash (`--`)?

---

`--nocapture` shows `println!` output even for passing tests.

Default behavior (output hidden):
```bash
$ cargo test
test test_with_output ... ok  # No output shown
```

With --nocapture:
```bash
$ cargo test -- --nocapture
Starting test...
Result is: 4
test test_with_output ... ok
```

The double dash (`--`) separates options:
```
cargo test -- --nocapture
           ↑  ↑
           |  Options for test binary
           Separator
```

- Before `--`: Options for cargo
- After `--`: Options for the test binary

Without `--`, cargo would try to interpret `--nocapture` itself and fail.

