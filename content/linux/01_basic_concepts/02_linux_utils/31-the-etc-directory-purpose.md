## The /etc Directory Purpose

What is stored in the `/etc` directory, and what are its key characteristics?

---

**Purpose:** Central repository for system-wide configuration files

**Key Characteristics:**
- **Text-based**: Most files are plain text (editable with vim/nano)
- **Root access required**: Typically need sudo/root to modify
- **System-wide impact**: Changes affect all users
- **Careful editing required**: Syntax errors can break system functionality
- **Backup critical**: Always backup before modifying

**Common contents:**
- System configuration files
- Network configuration
- User and group databases (`/etc/passwd`, `/etc/group`, `/etc/shadow`)
- Service configurations
- Security policies

