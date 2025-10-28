## CROSS JOIN Warning

Why should CROSS JOIN be used with caution, and what's a common mistake that accidentally creates one?

---

CROSS JOIN should be used with caution because it can create enormous result sets very quickly (multiplying row counts). A common mistake is forgetting the ON clause in a regular JOIN, which some SQL dialects interpret as a CROSS JOIN, potentially causing performance issues or unexpected results.

