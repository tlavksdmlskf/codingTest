-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME from ANIMAL_INS i, ANIMAL_OUTS o where i.ANIMAL_ID = o.ANIMAL_ID and  SEX_UPON_INTAKE like 'Intact%' and SEX_UPON_OUTCOME != SEX_UPON_INTAKE order by ANIMAL_ID