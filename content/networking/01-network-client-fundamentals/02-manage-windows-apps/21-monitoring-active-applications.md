## Monitoring Active Applications

How can administrators monitor running applications and their resource usage?

---

Use **Task Manager → Processes or Details** to view CPU, memory, and status; or PowerShell:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

