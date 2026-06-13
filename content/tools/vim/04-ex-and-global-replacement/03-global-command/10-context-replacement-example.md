## Context Sensitive Replacement Example

Write a command that changes `Esc` to `ESC`, but only on lines containing `class="keycap"`.

---

`:g/class="keycap"/s/Esc/ESC/g`

