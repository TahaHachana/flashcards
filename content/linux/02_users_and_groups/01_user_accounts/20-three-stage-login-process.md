## Three-Stage Login Process

Describe the three stages of the Linux login process. At which stage do most authentication problems occur?

---

**Stage 1: System Boot and Kernel Load**
- OS boots, kernel loads, services start
- System displays authentication prompt (login:)
- Issues: System won't boot, no prompt appears
- Usually works if you see login prompt

**Stage 2: Authentication and Validation** ← **MOST PROBLEMS OCCUR HERE**
- User enters username and password
- Linux checks /etc/passwd (account exists?)
- Linux checks /etc/shadow (password correct?)
- Linux checks account settings (expired? locked?)
- PAM policies evaluated
- Decision: Success (go to Stage 3) or Failure (return to login)

**Stage 3: Environment Setup and Shell Launch**
- System processes profile files (/etc/profile, ~/.bashrc)
- Applies user customizations (aliases, prompt, PATH)
- Launches user's default shell
- Issues: Invalid shell path, profile errors, permission problems

**Key Point**: Most authentication failures occur at Stage 2 during credential and account status validation.

