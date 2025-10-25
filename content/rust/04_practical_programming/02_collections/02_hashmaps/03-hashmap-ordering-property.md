## HashMap Ordering Property

Are keys in a HashMap ordered? What's the implication when iterating?

---

No, HashMap keys are unordered and appear in unpredictable order. Iteration order is not guaranteed and can change between program runs. If you need ordered keys, use BTreeMap instead.

