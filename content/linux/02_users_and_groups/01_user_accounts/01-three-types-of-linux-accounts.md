## Three Types of Linux Accounts

What are the three types of accounts in Linux, what are their UID ranges, and what is the purpose of each type?

---

1. **System Accounts**: UID 1-4 (UID 0 reserved for root). Represent parts of the Linux OS itself; various components have access to different resources.

2. **Service Accounts**: UID 100-999 (varies by distribution). Allow applications and services to access system resources (CPU, memory, networking). Example: Apache web server (httpd).

3. **User Accounts**: UID 1000+ (varies by distribution). Represent people authenticating to the system to access resources. Most commonly managed by administrators.

Note: UID ranges may vary between Linux distributions.

