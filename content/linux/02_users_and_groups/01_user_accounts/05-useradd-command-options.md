## useradd Command Options

What are the most common useradd options and what does each one do? Include the syntax format.

---

**Syntax**: `useradd -options username`

**Common Options**:
- **-c** "comment": Sets full name (use quotes if spaces)
- **-e** YYYY-MM-DD: Sets account expiration date
- **-m**: Creates home directory in /home
- **-s** /path/shell: Sets default login shell
- **-u** number: Sets specific UID
- **-D**: Displays default settings

**Example**: `useradd -c "Kai Garcia" -e 2025-12-31 -s /bin/ksh -m kgarcia`

**Critical Note**: useradd creates the account but does NOT set a password - must use passwd command separately.

