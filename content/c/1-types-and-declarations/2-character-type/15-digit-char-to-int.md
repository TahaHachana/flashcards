# How do you convert a `char` representing a digit to its corresponding integer value?

---

Subtract '0' from the `char`, e.g., `int num = c - '0';` where `c` is a `char` between '0' and '9'.