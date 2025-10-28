## Complex JOIN Conditions

Can JOIN conditions use operators other than equality, and can they include multiple conditions?

---

Yes. JOIN conditions can use any comparison operators (=, <, >, <=, >=, !=) and can combine multiple conditions using AND/OR. Examples include: range joins (`a.date BETWEEN b.start_date AND b.end_date`), inequality joins (`a.price > b.price`), and compound conditions joining on multiple columns (`a.year = b.year AND a.month = b.month`).

