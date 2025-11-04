## Group Entry Format in /etc/group

What do the fields in a `/etc/group` entry represent? For example: `development:x:1000:jmace`

---

The four fields separated by colons represent:
1. Group name (development)
2. Password placeholder - "x" indicates use of gshadow password file if password is assigned
3. Group ID number (1000)
4. Group members list (jmace) - comma-separated if multiple members, empty if no members

