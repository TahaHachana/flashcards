## Snapshots vs Delta Storage

How does Git store project versions differently from traditional delta-based version control systems?

---

Git stores complete snapshots of the entire project at each commit, not differences/deltas. Traditional systems store a base file plus a list of changes. Git's approach: each commit is a full picture of the project; unchanged files are linked to previous versions for efficiency.

