## Making Scripts Executable

How do you make a script executable and how do you run it from the current directory?

---

To make a script executable:
`chmod +x script_name.sh`

To execute it from the current directory:
`./script_name.sh`

The `./` tells Bash to check the current directory for the script, because your home directory typically isn't part of the PATH variable.

