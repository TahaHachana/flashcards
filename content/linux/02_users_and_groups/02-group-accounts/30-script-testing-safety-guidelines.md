## Script Testing Safety Guidelines

Where should you test account management scripts and why?

---

You should NEVER run account management scripts on production systems. Always test on:
- Test systems
- Virtual machines (VMs)
- Development servers
- Lab environments

This is critical because scripts can make system-wide changes, mistakes can affect multiple accounts, and you need to ensure scripts work as intended before risking production disruptions.

