## Returning to Command Mode

How do you return to command mode from insert mode, and what happens if you press ESC when already in command mode?

---

Press ESC to return to command mode. The cursor moves back one space (onto the last character typed).

If you are already in command mode when you press ESC, Vim beeps. This is why command mode is sometimes jokingly called "beep mode" — you can always press ESC until you hear the beep to confirm you are in command mode.

