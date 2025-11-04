## SUM Function Purpose

What does the SUM() aggregate function do, and what types of columns should it be used on?

---

SUM() adds up all numeric values in a column across the group, returning a single total. It works with numeric types (integers, decimals, floats). Only use SUM on columns where adding makes semantic sense, like amounts, quantities, or durations. Don't use it on IDs or other numbers that shouldn't be added together.

