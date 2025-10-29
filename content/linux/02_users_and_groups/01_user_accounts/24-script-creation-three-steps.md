## Script Creation Three Steps

What are the three basic steps to create and run a user management script in Linux?

---

**Step 1: Create Text Document**
- Use any text editor (vim, nano, etc.)
- Plain text format required
- Name it descriptively (e.g., create_users.sh)
- No special formatting needed

**Step 2: Enter Commands**
- Write commands as you would in terminal
- Add comments (# lines) for clarity
- Include shebang line (optional but recommended): `#!/bin/bash`
- Save and close file

**Step 3: Set Execute Permission**
- Command: `chmod +x scriptname.sh`
- Makes file executable
- Allows system to run the commands

**Running the Script**:
- `./scriptname.sh` (from current directory)
- `/path/to/scriptname.sh` (full path)
- `bash scriptname.sh` (explicit interpreter)

**Safety Note**: Test scripts on test systems or VMs first, never on production without testing.

