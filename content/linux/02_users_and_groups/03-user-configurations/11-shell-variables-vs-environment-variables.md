## Shell Variables vs Environment Variables

What is the critical difference between shell variables and environment variables, and how are they created and used differently?

---

**Shell Variables (Local Variables):**
- **Scope:** Current shell only
- **Inheritance:** NOT passed to child processes
- **Creation:** Simple assignment without `export`
- **Convention:** Usually lowercase
- **Persistence:** Lost when shell exits

**Example:**
```bash
my_variable="hello"
echo $my_variable        # Works in current shell

bash                      # Start subshell
echo $my_variable        # Empty - not inherited
exit
```

**Environment Variables:**
- **Scope:** Current shell AND all child processes
- **Inheritance:** Passed to child processes automatically
- **Creation:** Use `export` command
- **Convention:** Usually UPPERCASE
- **Persistence:** Inherited by spawned programs

**Example:**
```bash
export MY_VAR="shared value"
echo $MY_VAR             # Works in current shell

bash                      # Start subshell
echo $MY_VAR             # Works - inherited!
exit
```

**Key Distinction:**
Child processes receive a COPY of environment variables. Changes in the child don't affect the parent.

**Creation Methods:**
```bash
# Shell variable
VAR="value"

# Environment variable - Method 1
export VAR="value"

# Environment variable - Method 2
VAR="value"
export VAR
```

**Comparison Table:**

| Feature | Shell Variable | Environment Variable |
|---------|---------------|---------------------|
| **Scope** | Current shell only | Current shell + children |
| **Inheritance** | Not inherited | Inherited by child processes |
| **Creation** | `VAR=value` | `export VAR=value` |
| **Naming Convention** | Usually lowercase | Usually UPPERCASE |
| **Visibility** | Single shell session | Available to spawned programs |

**When to Use Each:**
- Shell variables: Temporary storage within single script/session
- Environment variables: Settings needed by child processes and programs

