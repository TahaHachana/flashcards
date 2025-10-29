## System Profile Processing Stage

During Stage 3 of the login process (Environment Setup), what profile files are processed and what types of customizations do they apply? What problems can occur here?

---

**Stage 3: Environment Setup and Shell Launch**

**Profile Files Processed** (in order):
1. System-wide profiles: `/etc/profile`, `/etc/bash.bashrc`
2. User-specific profiles: `~/.bash_profile`, `~/.bashrc`, `~/.profile`

**Customizations Applied**:
- User-specific command aliases (e.g., `alias ll='ls -la'`)
- User preferences and settings
- Custom command prompts (PS1 variable)
- PATH customizations (additional directories for commands)
- Environment variables (EDITOR, LANG, etc.)
- Shell options and functions
- Startup programs

**Shell Launch**:
- User's default shell from `/etc/passwd` executes
- Presents customized command prompt
- User ready to work

**Potential Problems at Stage 3**:

**Issues**:
- Invalid shell path (shell doesn't exist)
- Profile files contain syntax errors
- Permission issues on home directory
- Disk quota exceeded
- Resource limits reached

**Symptoms**:
- Authentication succeeds but user immediately logged out
- Shell doesn't start / no prompt appears
- Error messages about profile files
- "No directory, logging in with home=/" messages

**Example Problem**: `/etc/passwd` shows `/bin/kshh` (typo) → shell can't launch
**Solution**: `sudo usermod -s /bin/bash username`

