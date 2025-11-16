## Common Environment Variables

Describe the purpose and usage of the seven most important default environment variables in Linux.

---

**1. HOME**
- Purpose: User's home directory path
- Example: `/home/maria`
- Usage: `cd $HOME` or `cd ~` (tilde is shorthand for $HOME)

**2. USER**
- Purpose: Current username
- Example: `maria`
- Usage: `echo "Hello, $USER"` or conditional logic based on username

**3. PATH**
- Purpose: Colon-separated list of directories searched for executables
- Example: `/usr/local/bin:/usr/bin:/bin`
- How it works: Shell searches directories left to right when you type a command
- Modification: `export PATH=$PATH:/new/directory`

**4. SHELL**
- Purpose: Path to user's default login shell
- Example: `/bin/bash`
- Usage: Determine which shell is in use, shell-specific logic

**5. HOSTNAME**
- Purpose: System's network name
- Example: `server01.example.com`
- Usage: Identify which system you're on, conditional logic by server

**6. MAIL**
- Purpose: Location of user's mail file
- Example: `/var/mail/maria`
- Usage: Mail client configuration, checking for new mail

**7. HISTSIZE**
- Purpose: Number of commands stored in memory (current session)
- Example: `1000`
- Related: `HISTFILESIZE` - number of commands in `~/.bash_history` file
- Usage: `export HISTSIZE=5000` to increase command history buffer

**Viewing Variables:**
```bash
echo $HOME              # View specific variable
printenv                # View all environment variables
env                     # Alternative to view all variables
```

