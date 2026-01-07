## Main Thread Exits Early

What happens if the main thread exits while spawned threads are still running?

---

When main exits, the entire process terminates immediately, killing all spawned threads regardless of whether they've finished their work. Spawned threads won't complete - they're forcibly terminated. This can leave work incomplete, cause data corruption, or lose results. Always join threads you care about, or keep main alive until background work completes. The process exit is ungraceful for spawned threads.

