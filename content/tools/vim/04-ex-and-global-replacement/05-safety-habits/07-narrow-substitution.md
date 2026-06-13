## Ways To Narrow A Substitution

Name several ways to limit the blast radius of a substitution.

---

Use whole-word boundaries `\<...\>`, line anchors `^`/`$`, a line range (e.g. `:50,100s/.../.../`), and context with `:g/pattern/s/old/new/g`. The narrower the pattern, the fewer accidental matches.

