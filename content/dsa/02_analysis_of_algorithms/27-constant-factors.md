## Constant Factors in Big O

Why does Big O notation ignore constant factors and lower-order terms? When might constants actually matter in practice?

---

**Why ignore**:
- Focus on growth rate as n→∞
- Constants vary by implementation/hardware
- Asymptotic behavior is what scales

**Example**: 100n and n are both O(n)

**When constants matter**:
1. **Small input sizes**: 100n vs n makes huge difference when n=10
2. **Embedded systems**: Limited resources make constants critical
3. **Comparing same complexity**: O(n) vs O(n) might differ by factor of 100
4. **Real-time systems**: 0.001n might meet deadline while 10n doesn't

Big O is for scalability; real performance needs constant factor analysis too.

