## Struct Lifetime Checklist

What are the key steps when creating a struct with references?

---

1. Add lifetime parameter(s): `struct Foo<'a>`
2. Annotate reference fields: `field: &'a Type`
3. Match impl blocks: `impl<'a> Foo<'a>`
4. Constructors take references with same lifetime: `fn new(data: &'a Type) -> Self`
5. Methods returning references typically return `&'a Type` (part of struct's data)
6. Consider elision: Many method signatures can elide the `'a`

Following this checklist ensures correct lifetime usage in structs.

