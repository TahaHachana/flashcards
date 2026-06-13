## Scope With Whole Word Matching

How would you change "child" to "children" without affecting "childish"?

---

Use whole-word boundaries: `:%s/\<child\>/children/g`. The `\<` and `\>` anchor the match to a complete word.

