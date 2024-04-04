-- 코드를 입력하세요
select name, datetime from (SELECT i.name, i.datetime from ANIMAL_INS i, ANIMAL_OUTS o where i.animal_id = o.animal_id(+) and o.name is null and i.name is not null order by i.DATETIME)
where rownum <= 3