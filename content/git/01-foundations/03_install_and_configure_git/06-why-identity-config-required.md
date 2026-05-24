## Why Identity Configuration Is Required

Why is configuring `user.name` and `user.email` the first thing you must do after installing Git?

---

Git **embeds the author's name and email into every commit** as permanent, immutable metadata. Without this configuration:
- Git may use incorrect system defaults
- Some Git versions will refuse to make a commit
- Collaborators cannot identify who made which changes

Every commit stores: the snapshot, the author identity, a timestamp, and a commit message.

