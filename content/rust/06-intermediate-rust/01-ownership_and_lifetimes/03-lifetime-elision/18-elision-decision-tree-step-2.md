## Elision Decision Tree Step 2

After confirming a function has reference inputs, what's the next question in the elision decision tree?

---

"Does it return references?" If NO, Rule 1 applies (separate lifetimes for inputs), and you're done—lifetime relationships don't matter. If YES, you need to determine how many reference inputs there are and whether it's a method to see if Rules 2 or 3 apply.

