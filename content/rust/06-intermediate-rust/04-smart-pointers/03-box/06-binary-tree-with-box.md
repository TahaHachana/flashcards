## Binary Tree with Box

Implement a binary tree node structure using `Box` for the child nodes.

---

```rust
#[derive(Debug)]
struct TreeNode<T> {
    value: T,
    left: Option<Box<TreeNode<T>>>,
    right: Option<Box<TreeNode<T>>>,
}

fn main() {
    // Build tree:    5
    //               / \
    //              3   7
    let tree = TreeNode {
        value: 5,
        left: Some(Box::new(TreeNode {
            value: 3,
            left: None,
            right: None,
        })),
        right: Some(Box::new(TreeNode {
            value: 7,
            left: None,
            right: None,
        })),
    };
    
    println!("{:#?}", tree);
}
```

**Pattern:**
- Root node owns its data
- Children are `Option<Box<TreeNode<T>>>`
- `None` represents absence of a child
- Each `Box` allows recursive structure without infinite size

