## Appropriate Use of SUM

Why should you only use SUM() on certain types of numeric columns? Give examples of appropriate and inappropriate uses.

---

SUM should only be used on columns where addition makes business sense. Appropriate: SUM(amount) for total revenue, SUM(quantity) for total items. Inappropriate: SUM(customer_id) is meaningless (IDs shouldn't be added), SUM(price) is usually wrong (prices typically need to be multiplied by quantity first, not summed directly).

