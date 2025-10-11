## Loop Frequency Count Rule

For a top-tested loop "for i = low to high do", why does the loop header execute (high - low + 2) times while the body executes (high - low + 1) times?

---

The loop header executes one **extra time** to test the exit condition. 

- Body executes: (high - low + 1) times
- Header executes: (high - low + 1) + 1 = (high - low + 2) times

The additional test determines that the loop should terminate, so the header is evaluated one more time than the body is executed.

