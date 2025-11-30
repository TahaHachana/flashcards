## Key Fetch vs Pull Principles

What are the essential principles about fetch vs pull?

---

1. `fetch` downloads, doesn't merge (safe, read-only)
2. `pull` = fetch + merge (convenient, automatic)
3. Fetch updates remote tracking branches only
4. Pull updates working directory and current branch
5. Fetch is safer for reviewing before integrating
6. Pull is faster for quick synchronization
7. Both require internet connection
8. Configure pull behavior (merge, rebase, ff-only)
9. `fetch --prune` removes stale references
10. Use fetch for control, pull for convenience

Understanding the difference prevents surprises!

