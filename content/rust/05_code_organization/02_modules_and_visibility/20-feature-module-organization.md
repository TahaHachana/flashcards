## Feature Module Organization

How do you organize related functionality into feature modules? Provide an example.

---

**Pattern**: Group related constants, types, and functions into modules by feature or concern.

**Example**:
```rust
pub mod parser {
    pub fn parse(input: &str) -> Result<Ast, Error> {
        // Parsing logic
    }
}

pub mod validator {
    pub fn validate(ast: &Ast) -> Result<(), Error> {
        // Validation logic
    }
}

pub mod compiler {
    pub fn compile(ast: &Ast) -> Result<Bytecode, Error> {
        // Compilation logic
    }
}
```

**Benefits**:
- Clear separation of concerns
- Easy to navigate codebase
- Can understand purpose from module name
- Related code stays together

