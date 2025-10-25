## &str to String Conversion

What are three ways to convert &str to String and what is the performance cost?

---

Three ways:
1. to_string(): let owned = slice.to_string();
2. String::from(): let owned = String::from(slice);
3. to_owned(): let owned = slice.to_owned();

Performance: Expensive - allocates heap memory and copies data. All three methods do exactly the same thing.

