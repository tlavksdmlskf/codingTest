-- 코드를 입력하세요
SELECT CAR_TYPE, count(car_id) cars from CAR_RENTAL_COMPANY_CAR where OPTIONS like ('%시트%')  group by CAR_TYPE order by CAR_TYPE 