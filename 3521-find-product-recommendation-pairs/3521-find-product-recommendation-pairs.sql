-- Write your PostgreSQL query statement below
SELECT 
    p1.product_id AS product1_id, 
    p2.product_id AS product2_id,
    pi1.category AS product1_category,
    pi2.category AS product2_category,
    COUNT(DISTINCT p1.user_id) AS customer_count
FROM ProductPurchases p1
INNER JOIN ProductPurchases p2 ON p1.product_id <> p2.product_id
AND p1.user_id = p2.user_id
INNER JOIN ProductInfo pi1 ON p1.product_id = pi1.product_id
INNER JOIN ProductInfo pi2 ON p2.product_id = pi2.product_id
WHERE p1.product_id < p2.product_id
GROUP BY p1.product_id, p2.product_id, pi1.category, pi2.category
HAVING COUNT(DISTINCT p1.user_id) >= 3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC