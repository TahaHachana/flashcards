## Word Boundary Metacharacters

What do `\<` and `\>` match?

---

`\<` matches the beginning of a word and `\>` matches the end of a word (a boundary is a space or punctuation). `\<ac` matches `action`; `ac\>` matches `maniac`; neither matches `react`. They need not be used in matched pairs.

