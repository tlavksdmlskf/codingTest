-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, to_char(PUBLISHED_DATE,'yyyy-mm-dd') from AUTHOR a, BOOK b where a.AUTHOR_ID = b.AUTHOR_ID and CATEGORY like ('%경제%') order by PUBLISHED_DATE