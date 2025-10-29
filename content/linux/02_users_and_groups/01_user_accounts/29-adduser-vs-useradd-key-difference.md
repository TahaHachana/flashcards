## adduser vs useradd Key Difference

What is THE most important difference between adduser and useradd that affects account usability?

---

**THE Critical Difference - Password Handling**:

**useradd**:
- Does NOT prompt for password during creation
- Creates account but leaves it unusable
- Requires separate `passwd username` command
- Two-step process: create account, then set password

**adduser**:
- Automatically prompts for password during creation
- Creates fully usable account in one step
- Interactive process includes password setting
- One-step process: account creation includes password

**Why This Matters**:
- Most Linux systems won't allow login with blank password
- useradd accounts are NOT usable until passwd command run separately
- adduser accounts are immediately usable after creation
- Easy to forget passwd step with useradd, creating unusable accounts

**Example Workflows**:

**useradd** (two commands):
```bash
sudo useradd -m jsmith
sudo passwd jsmith      ← Must remember this!
```

**adduser** (one command):
```bash
sudo adduser jsmith     ← Prompts for password automatically
```

**Distribution**: adduser primarily on Debian-based systems; useradd on all distributions.

