## Compile With Make

How do you compile from within Vim and view the errors?

---

`:make [target]` runs make (via `makeprg`) and captures output in the special Quickfix List window. If it doesn't open automatically, use `:copen`.

