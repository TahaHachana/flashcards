## PS1 Variable and Command Prompt Customization

What is the PS1 variable and what are the most common escape sequences used to customize the Bash command prompt? Provide examples of their usage.

---

**PS1 (Prompt String 1)** is a shell variable that defines the appearance of the primary command prompt in Bash. It's customized in the `~/.bashrc` file.

**Common PS1 Escape Sequences:**
- `\u` - Current username
- `\h` - System hostname (short)
- `\w` - Current working directory (full path)
- `\W` - Current directory (basename only)
- `\$` - `$` for standard users, `#` for root
- `\t` - Current time (24-hour HH:MM:SS)
- `\d` - Current date
- `\n` - Newline character

**Example Configurations:**

Standard prompt:
```bash
PS1="\u@\h:\w\$ "
# Result: maria@server01:/home/maria/documents$
```

With timestamp:
```bash
PS1="[\t] \u@\h:\w\$ "
# Result: [14:23:45] maria@server01:/home/maria/documents$
```

**Critical Rules:**
1. Always use double quotes (not single quotes) to allow escape sequence interpretation
2. Include a trailing space for readability
3. The `\$` automatically shows `#` for root and `$` for regular users, providing visual distinction

