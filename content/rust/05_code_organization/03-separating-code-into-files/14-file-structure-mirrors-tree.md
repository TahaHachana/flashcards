## File Structure Should Mirror Module Tree

Why should file structure mirror the module tree, and what problems arise when they don't match?

---

**Best practice**: Keep file structure parallel to module tree

**Good alignment**:
```
Module tree:          File structure:
crate                 src/lib.rs
├── network           src/network.rs
│   ├── server        src/network/server.rs
│   └── client        src/network/client.rs
└── database          src/database.rs
```

**Problems when misaligned**:
- Developers can't find code easily
- Confusion about where to add new functionality
- File organization doesn't match mental model
- Harder onboarding for new team members

**Principle**: File location should match module path
- `crate::network::server` → `src/network/server.rs`
- Easy to navigate from path to file and vice versa

