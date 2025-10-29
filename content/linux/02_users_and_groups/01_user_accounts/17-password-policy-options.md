## Password Policy Options

What passwd command options set password expiration policies? Give example commands for: 90-day max age, 7-day min age, 14-day warning.

---

**Maximum Password Age** (expiration):
`sudo passwd -x 90 username`
Password must be changed every 90 days

**Minimum Password Age** (prevents cycling):
`sudo passwd -n 7 username`
Cannot change password more than once per 7 days (prevents reverting to old password)

**Warning Period**:
`sudo passwd -w 14 username`
User warned 14 days before password expires

**Force Password Change on Next Login**:
`sudo passwd --expire username`
User must change password immediately upon next login

**Combined Example**:
`sudo passwd -x 90 -n 7 -w 14 username`

**Verification**: Use `sudo chage -l username` (detailed, readable) or `sudo passwd -S username` (summary)

