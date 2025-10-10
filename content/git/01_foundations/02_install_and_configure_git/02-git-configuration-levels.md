## Git Configuration Levels

What are Git's three configuration levels, in order of precedence from highest to lowest?

---

1. Local (--local): Repository-specific, stored in `.git/config`
2. Global (--global): User-specific, stored in `~/.gitconfig`
3. System (--system): System-wide, stored in `/etc/gitconfig`

Higher precedence levels override lower ones. Most personal configuration uses --global.

