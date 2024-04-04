-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME from animal_ins i, animal_outs o where  o.animal_id = i.animal_id(+) and o.animal_id is not null and i.animal_id is null order by animal_id