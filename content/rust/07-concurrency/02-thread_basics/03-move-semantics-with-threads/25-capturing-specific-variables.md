## Capturing Specific Variables

How do you move only specific variables into a thread while leaving others accessible?

---

Explicitly bind the variables you want to move before the closure. Pattern: let keep = data1; let move_this = data2; thread::spawn({ let move_this = move_this; move || use move_this but not keep }). The inner let shadows the outer variable, moving only that one. The outer keep remains accessible. This gives fine-grained control over what gets moved vs what stays in parent scope.

