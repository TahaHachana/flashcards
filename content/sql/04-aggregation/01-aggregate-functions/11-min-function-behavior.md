## MIN Function Behavior

What does MIN() return, and what data types does it work with?

---

MIN() finds the minimum value in a column. It works with any comparable type: for numbers it returns the lowest value, for dates the earliest date, and for strings the alphabetically first value (based on collation). It ignores NULL values. Example: MIN(amount) might return 0.00, MIN(rental_date) might return '2005-05-24', MIN(last_name) might return 'ABNEY'.

