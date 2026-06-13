## No Tail Recursion

Why is `:ab PG This movie is rated PG` rejected?

---

The abbreviation cannot appear at the end of its own expansion — that would loop infinitely; Vim reports "No tail recursion."

