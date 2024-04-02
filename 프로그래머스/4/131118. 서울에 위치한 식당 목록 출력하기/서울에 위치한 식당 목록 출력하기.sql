-- 코드를 입력하세요
SELECT i.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, r.review_score from REST_INFO i, (select REST_ID, round(avg(review_score), 2) review_score from REST_REVIEW group by REST_ID) r where i.REST_ID = r.REST_ID and ADDRESS like '서울%'  order by r.REVIEW_SCORE desc, FAVORITES desc