## Why Data Races Are Catastrophic

Why are data races considered catastrophic, and what makes them different from other bugs?

---

Data races cause undefined behavior - literally anything can happen. They are: (1) Non-deterministic - manifest differently based on unpredictable thread timing, (2) Nearly impossible to debug or reproduce, (3) Silent - may corrupt data without immediate symptoms, (4) Optimizer-breaking - compilers assume no data races and optimize accordingly, potentially making things worse, and (5) Security risks - can bypass security checks or leak sensitive data.

