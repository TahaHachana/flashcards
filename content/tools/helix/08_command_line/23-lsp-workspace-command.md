## LSP Workspace Command

How does `:lsp-workspace-command` parse its arguments?

---

The first argument (if present) is parsed normally. The rest of the line is parsed as JSON values. Unlike `:toggle-option`, string arguments must be quoted. Example: `:lsp-workspace-command lsp.Command "foo" "bar"`.

