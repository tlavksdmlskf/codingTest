-- 코드를 입력하세요
select FLAVOR from (SELECT f.FLAVOR, sum(f.TOTAL_ORDER + j.TOTAL_ORDER ) as total from FIRST_HALF f, JULY j where j.FLAVOR = f.FLAVOR group by f.flavor order by total desc)
where rownum <= 3