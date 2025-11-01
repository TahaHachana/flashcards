## Logical vs Physical Module Organization

What is the difference between the logical module tree and the physical file structure?

---

**Logical module tree**: How modules are related and nested (declared with `mod`)
**Physical file structure**: Where the actual code files are stored

**Example**:
```
Logical tree:           Physical files:
crate                   src/lib.rs
├── network             src/network.rs
│   └── server          src/network/server.rs
└── database            src/database.rs
```

**Key insights**:
- They are separate concepts
- They should align for clarity, but don't have to match exactly
- The compiler cares about the logical tree
- Developers benefit from parallel structures
- Module tree is declared with `mod`, independent of files

