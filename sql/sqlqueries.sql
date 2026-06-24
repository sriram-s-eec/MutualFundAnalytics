-- 1. Top 10 highest NAV
SELECT * FROM fact_nav
ORDER BY nav DESC
LIMIT 10;


-- 2. Lowest NAV
SELECT * FROM fact_nav
ORDER BY nav ASC
LIMIT 10;


-- 3. Average NAV
SELECT AVG(nav) AS avg_nav FROM fact_nav;


-- 4. Total records
SELECT COUNT(*) FROM fact_nav;