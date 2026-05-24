## Install Git on macOS with Homebrew

What is the recommended way to install the latest Git on macOS using a package manager?

---

```bash
brew install git
```

Homebrew installs the latest upstream Git, independent of Apple's bundled version. Alternatively, running `git --version` on macOS will prompt you to install the Xcode Command Line Tools if Git is not already present.

