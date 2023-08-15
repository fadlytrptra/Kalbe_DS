-- Query 1
SELECT "Marital Status", AVG(age) AS avg_age
FROM public.case_study_customer
GROUP BY "Marital Status";

-- Query 2
SELECT gender, AVG(age) AS avg_age
FROM public.case_study_customer
GROUP BY gender;

-- Query 3
SELECT s.storename, SUM(t.qty) AS total_quantity
FROM public.case_study_transaction t
JOIN public.case_study_store s ON t.storeid = s.storeid
GROUP BY s.storename
ORDER BY total_quantity DESC
LIMIT 1;

-- Query 4
SELECT p."Product Name", SUM(t.totalamount) AS total_amount
FROM public.case_study_transaction t
JOIN public.case_study_product p ON t.productid = p.productid
GROUP BY p."Product Name"
ORDER BY total_amount DESC
LIMIT 1;


