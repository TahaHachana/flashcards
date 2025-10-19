## Why Clone Makes Cost Visible

Why does Rust require explicit .clone() calls?

---

Makes the cost visible. When you see .clone(), you know a potentially expensive operation is happening (heap allocation and data copying), helping identify optimization opportunities.

