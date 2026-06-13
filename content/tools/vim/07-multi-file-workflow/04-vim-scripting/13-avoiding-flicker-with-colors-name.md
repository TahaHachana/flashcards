## Avoiding Flicker With Colors Name

How do you avoid re-applying (and flickering) a color scheme that hasn't changed?

---

Check the global `colors_name` variable (set by `:colorscheme`) and only switch when it differs: `if g:colors_name !~ colorScheme | execute "colorscheme " . colorScheme | endif`.

