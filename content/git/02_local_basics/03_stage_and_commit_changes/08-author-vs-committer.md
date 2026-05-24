## Author vs. Committer

What is the difference between the Author and Committer fields in a Git commit, and in what workflow do they differ?

---

```
Author    → The person who originally wrote the change.
            Records when the work was done.

Committer → The person who recorded the commit in the
            repository. Records when it was committed.
```

In a **patch workflow**, a contributor emails a patch to a maintainer. The contributor is the **Author** (they wrote the code); the maintainer who applies the patch with `git am` or `git apply` becomes the **Committer**. For direct commits by a solo developer the two are always identical.

