## When Not To Use Separate Tables

When might you NOT separate data into multiple tables? Give an example of a one-to-one relationship.

---

One-to-one relationships: Both sides have at most one of the other.

Example: Person and Passport
- One person has one passport
- One passport belongs to one person

Options:

1. Single table (often best):
```
Persons:
person_id | name | passport_number | passport_expiry
```

2. Separate tables (if needed):
```
Persons:
person_id (PK) | name

Passports:
passport_id (PK) | person_id (FK, UNIQUE) | number | expiry
```

When to separate:
- Optional data (not everyone has passport)
- Different security requirements
- Very large columns that aren't always needed

When to combine:
- Data always goes together
- Simpler queries
- Most cases

One-to-one is rare; often indicates tables should be combined.

