## Common Clone Issues

What are three common issues when cloning and their solutions?

---

1. Permission denied (publickey):
   - Check SSH key added to platform
   - Test: `ssh -T git@github.com`
   - Or use HTTPS instead

2. Repository not found:
   - Verify URL is correct
   - Check if repository is private (need authentication)
   - Verify you have access permissions

3. Network/firewall issues:
   - Check internet connection
   - Use HTTPS if SSH blocked
   - Configure proxy if needed

Always read error messages—they tell you what's wrong.

