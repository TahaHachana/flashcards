## Diagnosing CPU Issues

How can administrators diagnose high CPU usage in Windows?

---

Use **Task Manager → Performance → CPU**, then the **Processes** tab to identify high-load apps.
Optionally, use PowerShell:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

