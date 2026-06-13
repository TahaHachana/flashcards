## Windo Substitution Example

Write a `:windo` command that fixes every occurrence of `myPoorlyCapitalizedClass` to `MyPoorlyCapitalizedClass` across all open windows.

---

`:windo %s/myPoorlyCapitalizedClass/MyPoorlyCapitalizedClass/g`

