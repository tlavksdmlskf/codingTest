-- 코드를 입력하세요
SELECT count(USER_ID) from USER_INFO where to_char(JOINED,'yyyy') = '2021' and AGE between 20 and 29