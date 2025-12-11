## Atomic Operations Platform Support

Are atomic operations available on all platforms? What should you know about Arc's portability?

---

**Generally available:** Atomic operations are widely supported and Arc works on most platforms.

**Notable exceptions:**
- PowerPC and MIPS with 32-bit pointers: no `AtomicU64`/`AtomicI64`
- Some ARM platforms (e.g., `armv5te`): limited atomic operations
- Very old or rare processors: may lack full atomic support

**Documentation quote:**
> "The atomic types here are all widely available, however, and can generally be relied upon existing."

**What this means for you:**
```rust
// This works on virtually all platforms
let arc = Arc::new(data);

// This works on most, but not all platforms
let arc_atomic_u64 = Arc::new(AtomicU64::new(0));
```

**Practical advice:**
- For modern systems (x86, ARM64, etc.): Don't worry about it
- For embedded/exotic platforms: Check documentation
- Arc itself is almost always available
- Some specific atomic types might not be

**Bottom line:** Unless you're targeting very old or rare hardware, Arc is available and works as expected.

