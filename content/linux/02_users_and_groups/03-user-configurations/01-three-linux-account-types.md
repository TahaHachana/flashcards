## Three Linux Account Types

What are the three types of user accounts in Linux, and what are the key characteristics of each type including UID ranges, login capability, and primary purpose?

---

**1. Root User Account (Superuser):**
- UID: 0 (this specific UID grants root privileges)
- Login: Yes, can be used for interactive login
- Purpose: Complete system control and administration
- Created automatically during installation
- Used for system configuration, updates, service management, and user/group administration

**2. Service Accounts (System Accounts):**
- UID: ≤500 or ≤1000 (varies by distribution)
- Login: No, cannot be used for interactive login
- Purpose: Run background services and system processes
- Created automatically during installation or service installation
- Names reflect their function (e.g., ftp, mail, apache, mysql)
- Enable resource management and security isolation

**3. Standard User Accounts:**
- UID: ≥501 or ≥1000 (varies by distribution)
- Login: Yes, can log in to the system
- Purpose: Interactive use by human users
- Created manually by administrators
- Human-readable usernames (e.g., maria, bjackson)
- Limited privileges - can manage own data and basic settings
- Cannot perform administrative tasks without privilege escalation

All account information is stored in `/etc/passwd` with password data in `/etc/shadow`.

