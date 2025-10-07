## Monitoring Windows Services

What distinguishes services from applications, and how are they monitored?

---

Services run in the background (no GUI) and support core functions. Use **Task Manager → Services** or PowerShell:

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
```

