-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME from ANIMAL_INS i, ANIMAL_OUTS o where i.animal_id = o.animal_id and i.DATETIME > o.DATETIME order by i.DATETIME