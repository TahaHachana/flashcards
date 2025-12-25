## Mock Server Test Pattern

How do you create a mock server for testing with automatic cleanup?

---

```rust
struct MockServer {
    port: u16,
    server_handle: ServerHandle,
}

impl MockServer {
    fn start() -> Self {
        let port = find_available_port();
        let server = start_test_server(port);
        MockServer {
            port,
            server_handle: server,
        }
    }
    
    fn url(&self) -> String {
        format!("http://localhost:{}", self.port)
    }
    
    fn expect_request(&self, path: &str, response: &str) {
        self.server_handle.mock(path, response);
    }
}

impl Drop for MockServer {
    fn drop(&mut self) {
        self.server_handle.stop();
    }
}

#[test]
fn test_api_call() {
    let server = MockServer::start();
    server.expect_request("/api/users", r#"{"users": []}"#);
    
    let response = make_request(&server.url());
    assert_eq!(response.status(), 200);
    // Server automatically stopped on drop
}
```

