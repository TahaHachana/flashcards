## Frequency Count Method Core Principle

In a priori analysis, why do we compute only frequency counts and ignore actual execution times of statements?

---

Ignoring execution times maintains **machine independence**. The time taken for a single statement execution depends on the machine's instruction set and configuration. By counting only how many times statements execute (frequency count), the analysis remains valid regardless of hardware, making results comparable across different systems.

