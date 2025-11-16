## The /etc/skel Directory

What is the `/etc/skel` directory, how does it work, and what are practical use cases for system administrators?

---

**Purpose:** `/etc/skel` (skeleton directory) serves as a template repository for new user accounts. Files placed here are automatically copied to each new user's home directory during account creation.

**How It Works:**
1. Administrator places template files in `/etc/skel`
2. When `useradd -m username` is executed, the system copies all files from `/etc/skel` to the new user's home directory
3. Files are assigned ownership to the new user
4. Permissions are preserved from `/etc/skel`

**Default Contents (typical):**
```
/etc/skel/.bash_logout
/etc/skel/.bashrc
/etc/skel/.profile
```

**Practical Use Cases:**

1. **Pre-configured Shell Settings:**
```bash
sudo vim /etc/skel/.bashrc
# Add company-standard aliases, prompts, history settings
```

2. **Policy Distribution:**
```bash
sudo cp acceptable_use_policy.txt /etc/skel/
```

3. **Standard Directory Structure:**
```bash
sudo mkdir -p /etc/skel/{Documents,Projects,Downloads}
```

4. **Development Environment Templates:**
```bash
sudo cp .vimrc .gitconfig .tmux.conf /etc/skel/
```

**Critical Limitations:**
- Only affects NEW users created AFTER files are added to `/etc/skel`
- Does NOT affect existing users
- To update existing users, must copy files manually

**Verification:**
```bash
sudo useradd -m testuser
sudo ls -la /home/testuser
# Should show all files from /etc/skel
```

