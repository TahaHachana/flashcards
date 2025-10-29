## Usernames vs UIDs

What is the difference between a username and a UID? Which does Linux actually use for access control, and why does this matter?

---

**Username**: Human-readable label administrators use (e.g., kgarcia, kaig, kai_garcia). Based on organizational preferences/standards.

**UID (User ID)**: Unique numeric identifier that Linux actually uses internally to manage accounts and control access.

**Key Point**: Linux compares the UID (not username) against resource permissions to grant or deny access. Usernames are for human convenience; UIDs are what the system works with.

**Why it matters**: If you delete and recreate an account with the same username, it gets a different UID and won't have access to the old user's files.

