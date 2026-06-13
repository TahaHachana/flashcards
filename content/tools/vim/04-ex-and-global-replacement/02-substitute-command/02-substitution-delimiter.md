## The Substitution Delimiter

In `:s/old/new/`, what is the role of `/`, and when can the trailing one be omitted?

---

The `/` is the delimiter separating the parts of the command. The trailing delimiter is optional when it is the last character on the line (so `:s/old/new` works). Almost any punctuation character can serve as the delimiter.

