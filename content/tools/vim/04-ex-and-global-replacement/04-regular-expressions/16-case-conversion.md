## Case Conversion In Replacements

What do `\u`, `\l`, `\U`, `\L`, and `\e`/`\E` do in a replacement string?

---

`\u`/`\l` uppercase/lowercase the next single character. `\U`/`\L` uppercase/lowercase all following characters until `\e` or `\E` ends the case change (or until the end of the replacement).

