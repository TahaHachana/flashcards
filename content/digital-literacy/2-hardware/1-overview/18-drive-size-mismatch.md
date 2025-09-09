# Drive size: marketed vs reported

Why does a 500 GB drive show ~465.66 GiB in the OS?

---

Manufacturers use decimal (500×10^9 bytes); OS reports in GiB: 500,000,000,000 ÷ 2^30 ≈ 465.661287 GiB.