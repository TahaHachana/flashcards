## Getting the Nth Character

How do you get the nth character from a string and what is its time complexity?

---

```rust
fn get_char_at(s: &str, n: usize) -> Option<char> {
    s.chars().nth(n)
}

let s = String::from("你好世界");
println!("{:?}", get_char_at(&s, 0));  // Some('你')
println!("{:?}", get_char_at(&s, 2));  // Some('世')
```
Time complexity: O(n), not O(1) like array indexing, because it must scan through previous characters.

