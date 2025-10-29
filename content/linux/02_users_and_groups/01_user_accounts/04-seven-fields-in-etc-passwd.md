## Seven Fields in /etc/passwd

List and explain the seven colon-separated fields in an /etc/passwd entry.

---

Format: `username:x:UID:GID:comment:home_directory:login_shell`

1. **Username**: Login name (e.g., kgarcia)
2. **Password Placeholder**: "x" indicates password is in /etc/shadow
3. **UID**: User ID number - unique identifier Linux uses
4. **GID**: Primary group ID number
5. **Comment (GECOS)**: Usually full name, can include contact info
6. **Home Directory**: Absolute path (e.g., /home/kgarcia)
7. **Login Shell**: Default shell path (e.g., /bin/bash)

Example: `kgarcia:x:1001:1001:Kai Garcia:/home/kgarcia:/bin/ksh`

