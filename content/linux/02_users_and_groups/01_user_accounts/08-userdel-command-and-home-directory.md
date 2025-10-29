## userdel Command and Home Directory

What does userdel do by default, and how does the -r option change its behavior? Why might you NOT want to use -r?

---

**Default Behavior**: `userdel username`
- Removes account from /etc/passwd and /etc/shadow
- User cannot log in
- Home directory REMAINS on system with all files

**With -r Option**: `userdel -r username`
- Removes account
- Deletes home directory
- Removes all files in home directory
- Deletes mail spool
- PERMANENT and IRREVERSIBLE

**Why Preserve Home Directory**:
- User data may need to be assigned to other users
- Files might be needed for business continuity
- Important documents shouldn't be accidentally deleted
- Allows data review before permanent deletion

**Warning**: Deleted accounts cannot be recovered. Recreating produces different UID, causing ownership/permission issues.

