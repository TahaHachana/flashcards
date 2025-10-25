## Multiple Selections Clipboard Behavior

What happens when you yank multiple selections to the clipboard registers (`+` or `*`)?

---

The selections are joined with newlines. When pasting, if the clipboard was last yanked by the current Helix session, it pastes as multiple selections. Otherwise, clipboard contents are pasted as one selection.

