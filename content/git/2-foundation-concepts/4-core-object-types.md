# Git’s Four Core Object Types

What are Git’s four core object types?

---

- Blob: raw file data (content only)  
- Tree: directory listing mapping names and modes to blobs/trees  
- Commit: snapshot pointing to a tree plus metadata and parent(s)  
- Tag: named reference to any object (annotated or lightweight)

Example—inspect a blob:

```bash
git cat-file -p <blob_sha>
```
