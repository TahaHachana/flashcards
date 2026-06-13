## Inverting The Match

How do you run a command on lines that do NOT contain a pattern?

---

Use `:g!` or its synonym `:v`. For example, `:v/#include/d` deletes every line that is not an "#include" line.

