## Conflict Resolution Strategies

What are four strategies for resolving a conflict between two versions?

---

Given conflict:
```javascript
<<<<<<< HEAD
console.log("Welcome to our app!");
=======
console.log("Welcome, user!");
>>>>>>> feature
```

1. Keep current (ours): `"Welcome to our app!"`
2. Keep incoming (theirs): `"Welcome, user!"`
3. Combine both: `"Welcome to our app, user!"`
4. Write new solution: `console.log(\`Welcome ${username}!\`);`

Choose based on understanding both changes and requirements.

