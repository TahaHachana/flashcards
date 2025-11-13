## SSH Authentication Setup

How do you set up SSH authentication for cloning?

---

1. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. Add to SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

3. Add public key to GitHub/GitLab:
   - Copy: `cat ~/.ssh/id_ed25519.pub`
   - Add in Settings → SSH keys

4. Test: `ssh -T git@github.com`

5. Clone: `git clone git@github.com:user/project.git`

