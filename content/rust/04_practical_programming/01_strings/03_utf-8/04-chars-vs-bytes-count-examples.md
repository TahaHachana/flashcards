## Chars vs Bytes Count Examples

What are the character counts and byte counts for these strings?
```rust
"hello"
"señor"
"你好"
"😀🦀"
```

---

"hello": 5 chars, 5 bytes (ASCII, 1 byte each)
"señor": 5 chars, 6 bytes (ñ is 2 bytes)
"你好": 2 chars, 6 bytes (3 bytes each)
"😀🦀": 2 chars, 8 bytes (4 bytes each emoji)

