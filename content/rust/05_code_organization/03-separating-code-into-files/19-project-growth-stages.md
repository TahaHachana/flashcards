## Project Growth Stages

How does file organization typically evolve as a Rust project grows?

---

**Stage 1 - Single file**:
```
src/lib.rs  (all code here)
```
**Good for**: Initial prototyping, tiny projects

**Stage 2 - Flat split**:
```
src/
├── lib.rs
├── parser.rs
├── compiler.rs
└── validator.rs
```
**Good for**: Small-medium projects with clear features

**Stage 3 - Hierarchical**:
```
src/
├── lib.rs
├── frontend/
│   ├── parser.rs
│   └── lexer.rs
└── backend/
    ├── codegen.rs
    └── optimizer.rs
```
**Good for**: Larger projects with distinct subsystems

**Key point**: The logical module tree can remain the same—you're just organizing the physical files better as complexity grows.

