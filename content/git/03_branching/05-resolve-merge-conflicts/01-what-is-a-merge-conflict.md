## What is a Merge Conflict

What is a merge conflict and when does it occur?

---

A merge conflict occurs when Git cannot automatically resolve differences between two branches. This happens when:
- Both branches modify the same lines in the same file
- One branch deletes a file while another modifies it
- Both branches create files with the same name
- Both branches modify binary files

Git pauses the merge and asks you to manually decide which changes to keep. Conflicts are normal in collaborative development.

