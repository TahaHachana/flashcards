## Installing and Updating Rust with rustup

How do you install or update the Rust toolchain using `rustup`?

---

Install Rust:

```bash
curl https://sh.rustup.rs -sSf | sh
```

Update toolchains:

```bash
rustup update
rustup default stable
```

Install nightly:

```bash
rustup install nightly
rustup override set nightly
```

