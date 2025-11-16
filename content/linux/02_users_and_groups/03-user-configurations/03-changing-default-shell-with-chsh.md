## Changing Default Shell with chsh

How does the `chsh` command work, what are its requirements and restrictions, and when do changes take effect?

---

**Purpose:** The `chsh` (change shell) command allows users to change their default login shell without directly editing `/etc/passwd`.

**Common Options:**
- `-l` or `--list-shells` - Display available shells
- `-s SHELL` or `--shell SHELL` - Specify new shell

**Syntax Examples:**
```bash
chsh -l                    # List available shells
chsh -s /bin/zsh          # Change to Zsh
chsh -s /bin/ksh          # Change to Korn shell
```

**Requirements and Restrictions:**

1. **Shell Must Be in /etc/shells:** The requested shell must appear in the `/etc/shells` whitelist (prevents security vulnerabilities)

2. **Full Path Required:** Must provide complete path (e.g., `/bin/zsh`, not just `zsh`)

3. **Authentication Required:** User must provide their password

4. **Takes Effect on Next Login:** Changes don't apply immediately - user must log out completely and log back in

5. **Root Can Change Any User's Shell:**
```bash
sudo chsh -s /bin/zsh username
```

**Where It's Stored:**
The shell is stored in the seventh field of `/etc/passwd`:
```
maria:x:1001:1001:Maria Garcia:/home/maria:/bin/bash
```

Users cannot edit `/etc/passwd` directly, which is why `chsh` is necessary.

