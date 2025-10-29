## Exit Codes for User Commands

How do you check if a user management command succeeded or failed? What do exit codes 0, 9, and 6 indicate?

---

**Check Exit Code**: `echo $?` (displays exit code of most recent command)

**Exit Code Meanings**:
- **0**: Success - command completed without errors
- **Non-zero**: Error occurred

**Common Exit Codes**:

**useradd**:
- 1: Couldn't update /etc/passwd
- 9: Username already in use
- 12: Couldn't create home directory

**usermod/userdel**:
- 1: Couldn't update /etc/passwd
- 2: Invalid command syntax
- 6: Specified user doesn't exist
- 8: Cannot modify/delete - user currently logged in

**All executables have exit codes** - use echo $? to check success/failure.

