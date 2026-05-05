## Troubleshooting — Stuck in ex Line-Editing Mode

You invoke Vim but see a colon prompt (`:`) instead of the normal screen. What happened and how do you fix it?

---

You are in ex line-editing mode, likely because an interrupt (CTRL-C) was received before Vim could draw the screen.

Fix: type `vi` and press ENTER at the colon prompt.

This switches ex into its visual (vi) mode and draws the normal Vim screen.

