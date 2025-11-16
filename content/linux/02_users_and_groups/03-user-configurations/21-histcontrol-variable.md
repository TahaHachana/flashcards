## HISTCONTROL Variable

What is the HISTCONTROL variable, what are its different options, and how do they affect command history management?

---

**Purpose:** HISTCONTROL controls how duplicate commands and space-prefixed commands are handled in history.

**HISTCONTROL Options:**

**1. ignoredups - Ignore Consecutive Duplicates**
```bash
export HISTCONTROL=ignoredups
```
- Removes consecutive duplicate commands
- Does NOT remove non-consecutive duplicates

**Example:**
```bash
# Commands: whoami, whoami, ls, whoami
# History shows: whoami, ls, whoami
```

**2. ignorespace - Ignore Space-Prefixed Commands**
```bash
export HISTCONTROL=ignorespace
```
- Commands starting with space are NOT saved
- Useful for sensitive commands (passwords, API keys)

**Example:**
```bash
 mysql -u admin -p SecretPassword
# This command won't appear in history (note leading space)
```

**3. ignoreboth - Combine Both**
```bash
export HISTCONTROL=ignoreboth
```
- Ignores consecutive duplicates
- Ignores space-prefixed commands
- **Most commonly recommended setting**

**4. erasedups - Remove ALL Duplicates**
```bash
export HISTCONTROL=erasedups
```
- When command is entered, removes ALL previous instances
- Only most recent instance remains
- Keeps history completely duplicate-free

**Example:**
```bash
# Commands: ls, cd /tmp, whoami, ls, cat file, ls
# History shows: cd /tmp, whoami, cat file, ls (only last 'ls')
```

**Combining Options:**
```bash
export HISTCONTROL=ignoreboth:erasedups
# Combines multiple features
```

**Default Behavior (Without HISTCONTROL):**
Every command is saved, including all duplicates:
```bash
# History shows:
715  whoami
716  whoami
717  whoami  # All three saved
```

**Recommended Configuration:**
```bash
# Add to ~/.bashrc
export HISTCONTROL=ignoreboth
```

**Benefits:**
- Cleaner history (no consecutive duplicates)
- Privacy for sensitive commands (space prefix)
- More useful command history overall

