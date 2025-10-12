## PowerShell Admin vs Standard Access

What are the key differences between standard PowerShell and Administrative PowerShell, and what is the recommended best practice?

---

**Key Differences**:
- **Standard PowerShell**: Opens in user profile directory with regular privileges
- **Admin PowerShell**: Opens in Windows\System32 directory; requires authentication; has full system access including registry navigation, software installation, and network device management

**Best Practice**: Spend most time in non-administrative PowerShell and only assert administrative privileges when necessary. Working constantly as administrator increases risk of errors and security issues.

