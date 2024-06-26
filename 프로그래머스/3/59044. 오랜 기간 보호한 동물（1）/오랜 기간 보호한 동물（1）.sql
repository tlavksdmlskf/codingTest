SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS a
LEFT JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE (b.NAME IS NULL) AND (a.NAME IS NOT NULL)
ORDER BY a.DATETIME
FETCH FIRST 3 ROWS ONLY;