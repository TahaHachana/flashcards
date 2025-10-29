## Account Information Display Commands

Compare the commands whoami, who, w, and id. What does each display and when would you use each?

---

**whoami**:
- Displays current user's username only
- Use when prompt doesn't show username or after su command

**who**:
- Shows all currently logged-in users (basic info)
- Displays: username, terminal, login time, source IP
- Use for simple check of who's online

**w**:
- Shows all logged-in users (detailed info)
- Includes: idle time, CPU usage, current process
- Use before system restarts to warn users
- **Idle time** particularly useful to identify inactive sessions

**id [username]**:
- Shows UID, GID, and group memberships
- For current user or specified user
- Use for troubleshooting permissions or verifying group membership

**Key Difference**: who/w show current sessions; whoami/id show account details.

