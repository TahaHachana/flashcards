## Delete Fold Vs Delete Text

What is the dangerous difference between `zd` and `dd` on a folded line?

---

`zd` deletes (undefines) the fold but leaves the text intact. `dd` on a folded line deletes ALL the lines hidden in the fold. Never confuse "delete fold" with "delete text".

