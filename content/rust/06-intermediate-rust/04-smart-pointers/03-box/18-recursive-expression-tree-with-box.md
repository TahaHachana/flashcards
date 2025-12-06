## Recursive Expression Tree with Box

Create an arithmetic expression evaluator using `Box` for recursive expressions. Support numbers, addition, and multiplication.

---

```rust
#[derive(Debug)]
enum Expression {
    Number(i32),
    Add(Box<Expression>, Box<Expression>),
    Multiply(Box<Expression>, Box<Expression>),
}

fn eval(expr: &Expression) -> i32 {
    match expr {
        Expression::Number(n) => *n,
        Expression::Add(left, right) => {
            eval(left) + eval(right)
        }
        Expression::Multiply(left, right) => {
            eval(left) * eval(right)
        }
    }
}

fn main() {
    // Build: (2 + 3) * 4 = 20
    let expr = Expression::Multiply(
        Box::new(Expression::Add(
            Box::new(Expression::Number(2)),
            Box::new(Expression::Number(3)),
        )),
        Box::new(Expression::Number(4)),
    );
    
    println!("Result: {}", eval(&expr));  // 20
}
```

**Pattern:** Recursive data structures for tree-like computations (parsers, compilers, interpreters).

