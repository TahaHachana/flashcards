## Case Sensitivity Of Searches

Are pattern searches case sensitive by default, and how do you match both cases?

---

Yes, searches are case sensitive by default (a search for "the" does not find "The"). Match both with a character class like `[Tt]he`, or turn on ignorecase with `:set ic`.

