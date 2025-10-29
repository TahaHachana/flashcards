## usermod Command Usage

What does the usermod command do, and what are three common modifications you can make with it? Include example commands.

---

**Purpose**: Modifies existing user accounts (cannot modify accounts with running processes)

**Common Modifications**:

1. **Change comment/full name**:
   `usermod -c "Joseph Deng" jdeng`

2. **Set account expiration**:
   `usermod -e 2027-12-31 alee`
   (Account cannot authenticate after this date but is NOT deleted)

3. **Change default shell**:
   `usermod -s /bin/ksh kgarcia`

**Other Options**: -d (home directory), -g (primary group), -L (lock), -U (unlock)

**Critical Limitation**: Will NOT modify accounts with running processes - user must log out first.

