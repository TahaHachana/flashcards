## Mock Object Pattern with RefCell

Why is `RefCell` perfect for mock objects in tests? Provide an example.

---

**Why RefCell is perfect for mocks:**
- Test APIs often require `&self` not `&mut self`
- Need to track calls, arguments, return values
- Must mutate internal state through immutable reference
- Single-threaded (tests run in one thread)

**Example:**
```rust
use std::cell::RefCell;

struct MockDatabase {
    calls: RefCell<Vec<String>>,
    query_results: RefCell<Vec<String>>,
}

impl MockDatabase {
    fn new() -> Self {
        MockDatabase {
            calls: RefCell::new(vec![]),
            query_results: RefCell::new(vec!["result1".into()]),
        }
    }
    
    // Takes &self to match real database API
    fn query(&self, sql: &str) -> Option<String> {
        // Track the call
        self.calls.borrow_mut().push(sql.to_string());
        
        // Return canned result
        self.query_results.borrow_mut().pop()
    }
    
    // Verification methods
    fn was_called_with(&self, sql: &str) -> bool {
        self.calls.borrow().contains(&sql.to_string())
    }
    
    fn call_count(&self) -> usize {
        self.calls.borrow().len()
    }
}

#[test]
fn test_user_service() {
    let mock_db = MockDatabase::new();
    
    // Use mock in test
    let result = mock_db.query("SELECT * FROM users");
    
    // Verify behavior
    assert!(mock_db.was_called_with("SELECT * FROM users"));
    assert_eq!(mock_db.call_count(), 1);
}
```

**Pattern benefits:**
- Matches production API (`&self`)
- Tracks test interactions
- Enables verification
- No need for `&mut`

