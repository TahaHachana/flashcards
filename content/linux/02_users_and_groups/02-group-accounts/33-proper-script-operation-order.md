## Proper Script Operation Order

What is the proper order of operations in an account management script?

---

The proper order is:
1. Create users first (using `useradd`)
2. Create groups second (using `groupadd`)
3. Add users to groups last (using `usermod -aG`)

This sequence ensures that both users and groups exist before attempting to establish membership relationships.

