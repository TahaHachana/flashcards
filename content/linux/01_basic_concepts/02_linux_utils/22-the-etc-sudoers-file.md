## The /etc/sudoers File

What is the `/etc/sudoers` file, and what is the proper way to edit it?

---

**Purpose:**
- Central configuration file for sudo permissions
- Defines which users/groups can run which commands
- Specifies exactly what root-level tasks are permitted

**Proper editing method:**
- **NEVER edit directly** with vim or nano
- **ALWAYS use:** `sudo visudo`
- `visudo` prevents syntax errors that could lock out administrators
- Performs validation before saving changes

**Why this matters:** A syntax error in `/etc/sudoers` could prevent all sudo access and lock you out of administrative functions.

