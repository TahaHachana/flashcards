## #[ignore] Common Use Cases

What are common scenarios for using `#[ignore]` in tests?

---

1. **Network/External Dependencies:**
```rust
#[test]
#[ignore]
fn test_api_endpoint() {
    let response = reqwest::blocking::get("https://api.example.com").unwrap();
    assert!(response.status().is_success());
}
```

2. **Expensive Operations:**
```rust
#[test]
#[ignore]
fn test_large_dataset() {
    // Processes 1GB of data, takes 10 minutes
    let results = process_huge_file("dataset.csv");
    assert_eq!(results.len(), 1_000_000);
}
```

3. **Platform-Specific:**
```rust
#[test]
#[ignore]
#[cfg(target_os = "windows")]
fn test_windows_api() {
    use_windows_specific_feature();
}
```

4. **Temporarily Broken:**
```rust
#[test]
#[ignore]  // TODO: Fix after database refactor (issue #123)
fn test_authentication() {
    // Currently broken, will fix soon
}
```

Document why with comments or `#[ignore = "reason"]`.

