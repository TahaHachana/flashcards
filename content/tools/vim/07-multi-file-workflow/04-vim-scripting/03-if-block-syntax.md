## If Block Syntax

What is the syntax of a Vim `if` block, and which parts are optional?

---

```vim
if cond
  " code
elseif other_cond
  " code
else
  " code
endif
```
The `elseif` (repeatable) and `else` blocks are optional; the block always ends with `endif`.

