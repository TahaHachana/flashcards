## UTF-8 Backward Compatibility

How is UTF-8 backward compatible with ASCII?

---

UTF-8 ASCII characters (0-127) have the exact same byte values as ASCII encoding. This means:
- Pure ASCII text is valid UTF-8
- Old tools expecting ASCII work with UTF-8 strings containing only ASCII
- No conversion needed for ASCII-only text

This is a huge practical advantage for compatibility with legacy systems.

