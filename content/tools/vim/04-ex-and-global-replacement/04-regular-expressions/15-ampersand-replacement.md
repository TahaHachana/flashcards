## The Ampersand In Replacements

What does `&` do in the replacement part of a substitution?

---

It replays the entire matched text ("the same thing"). For example, `:%s/Fortran/\U&/` uppercases "Fortran" by replaying the match.

