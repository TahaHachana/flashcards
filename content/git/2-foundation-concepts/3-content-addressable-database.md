# Content-Addressable Database

How does Git’s content-addressable database work?

---

Each object is named by the SHA-1 hash of its content and stored under `.git/objects/xx/yyyy…`. This model ensures immutability, integrity, and deduplication of data.
