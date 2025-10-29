## Script Variables and Comments

In a bash script for user creation, what are variables and comments? How do you identify each, and why are they important?

---

**Variables**:
- Placeholders for values identified by $ prefix
- Example: `$username`
- Allow scripts to work with different values
- Enable automation and reusability

**Example Usage**:
```bash
while read username; do
    useradd -c "$username" $username
done < userlist.txt
```
The `$username` gets replaced with each line from file.

**Comments**:
- Lines preceded by # character
- Not executed by system - for humans only
- Explain purpose, document settings, clarify sections
- Essential for collaboration and future reference

**Example**: `# This script creates developer accounts`

**Best Practice**: Comment extensively for complex scripts, unusual settings, or scripts shared with others.

