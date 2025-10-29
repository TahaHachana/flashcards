## useradd vs adduser

Compare useradd and adduser commands. What are the key differences, and when should you use each?

---

**useradd** (All distributions):
- Command-line driven, no prompts
- Does NOT automatically set password
- Requires separate passwd command
- Better for scripts/automation
- More control through options

**adduser** (Debian-based):
- Interactive with prompts for details
- Automatically prompts for password
- More user-friendly
- Modified interface to useradd
- Better for manual account creation

**Key Difference**: adduser prompts for password during creation; useradd requires separate passwd command.

**Installation**: Can install adduser on Red Hat systems: `dnf install adduser` or `apt-get install adduser`

