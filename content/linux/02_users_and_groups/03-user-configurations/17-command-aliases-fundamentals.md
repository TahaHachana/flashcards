## Command Aliases Fundamentals

What are command aliases, how do they differ from variables, and what is the correct syntax for creating them?

---

**What Are Aliases:**
Command aliases are user-defined shortcuts that represent longer, more complex commands with their options and arguments.

**Purpose:**
- Reduce typing for frequently-used commands
- Create memorable shortcuts for complex command sequences
- Customize command-line environment
- Prevent errors by standardizing command options

**Aliases vs. Variables:**

| Feature | Aliases | Variables |
|---------|---------|-----------|
| Purpose | Shortcut for commands | Store information |
| Function | Execute as commands | Hold values |
| Example | `alias ll='ls -la'` | `USER=kgarcia` |
| Usage | Command substitution | Value retrieval |

**Correct Syntax:**
```bash
alias name='command with options'
```

**Critical Syntax Rules:**

**1. No Spaces Around Equals Sign**
```bash
# CORRECT:
alias ll='ls -la'

# INCORRECT:
alias ll = 'ls -la'
```

**2. Quote the Command**
```bash
alias myls='ls -al'
```

**3. Use Meaningful Names**
```bash
# Good:
alias ll='ls -la'
alias cls='clear'

# Poor:
alias x='ls -la'
```

**Creating and Using Aliases:**
```bash
# Create
alias myls='ls -al'

# Use (shell expands to 'ls -al')
myls

# View all aliases
alias

# View specific alias
alias myls
```

**Key Distinction from Variables:**
- **Variables** store values: `BACKUP_DIR=/backup` then `cp file $BACKUP_DIR`
- **Aliases** substitute commands: `alias backup='cp file /backup'` then `backup`

