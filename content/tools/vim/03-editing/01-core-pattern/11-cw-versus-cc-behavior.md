## cw Versus cc Behavior

In original vi, how does a sub-line change (`cw`) behave differently from a whole-line change (`cc`)?

---

`cw` marks the end of the affected text with `$` and lets you type over the old text. `cc` wipes the line first, leaving a blank line to insert on. (In Vim's nocompatible mode, both just delete and enter insert mode.)

