## Snapshots vs. Deltas

How does Git store data differently from most other VCS tools like SVN?

---

Most VCS tools store data as a **list of file-based changes (deltas)** over time.

Git stores data as **snapshots** — at each commit, Git takes a picture of all files and stores a reference to that snapshot. If a file hasn't changed, Git stores a link to the previous identical version rather than the file again. Git thinks of data more like a **mini filesystem**.

