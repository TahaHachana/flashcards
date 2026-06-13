## Alternate Delimiter For Paths

Write a command that changes the path `/user1/tim` to `/home/tim` everywhere, using a delimiter other than `/`.

---

`:%s;/user1/tim;/home/tim;g` — using `;` as the delimiter lets the slashes inside the paths stay literal, avoiding backslash escaping.

