# Commenting Parameters

What's a good practice for commenting function parameters?

---

Use documentation comments to explain parameters:
```rust
/// Calculates the area of a rectangle
///
/// # Arguments
/// * `width` - The width in pixels
/// * `height` - The height in pixels
fn area(width: u32, height: u32) -> u32 {
    width * height
}
```