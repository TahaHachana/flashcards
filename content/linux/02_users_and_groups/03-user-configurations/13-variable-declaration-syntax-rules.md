## Variable Declaration Syntax Rules

What are the critical syntax rules for declaring and referencing variables in Bash? What happens if these rules are violated?

---

**Declaration Syntax Rules:**

**Rule 1: NO Spaces Around Equals Sign**
```bash
# CORRECT:
my_name=kgarcia
PATH=/usr/bin:/bin

# INCORRECT (causes errors):
my_name = kgarcia        # Error: my_name: command not found
my_name= kgarcia         # Error
my_name =kgarcia         # Error
```

**Why:** Shell interprets spaces as command separators. With spaces, Bash tries to execute the variable name as a command.

**Rule 2: Quote Values with Spaces**
```bash
# CORRECT:
MESSAGE="Welcome to the system"

# INCORRECT:
MESSAGE=Welcome to the system    # Interpreted as multiple commands
```

**Rule 3: Variables Are Case-Sensitive**
```bash
name=maria          # Different variable
NAME=maria          # Different variable
Name=maria          # Different variable
```

**Referencing Variables:**

**Use Dollar Sign ($) to Access Values:**
```bash
# Declaration (no $)
username=kgarcia

# Reference (with $)
echo $username              # Output: kgarcia
echo username               # Output: username (literal text)
```

**Optional Curly Braces for Clarity:**
```bash
echo ${username}            # Same as $username
echo ${username}_backup     # Avoids ambiguity
```

**Making Environment Variables:**
```bash
# Local variable (current shell only)
MY_VAR="value"

# Environment variable (inherited by children)
export MY_VAR="value"
```

**The Rule:**
- **Setting:** NO dollar sign
- **Getting:** YES dollar sign

