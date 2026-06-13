## Spot Editing Loop Alternative

When you want to change only some matches (not all), what vi loop lets you decide case by case?

---

The `n` (repeat search) and `.` (repeat last change) loop. For example: `/which` then `cwthat ESC`, then press `n` to find the next match and `.` to apply the same change only where appropriate.

