## What Filtering Does To The Buffer

When you filter a block of text through a Unix command in Vim, what happens to the original block?

---

The block is sent to the command as standard input, and the command's standard output REPLACES the original block in the buffer. The original text is gone (recoverable only with undo).

