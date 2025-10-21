## Expansion Syntax

What is the general syntax for expansions in Helix's command line?

---

Expansions start with `%` and follow the pattern: `%[<kind>]<open><contents><close>`. For example, `%sh{echo hi!}` where `sh` is the kind, and `{}`are the delimiters.

