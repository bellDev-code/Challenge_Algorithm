/*성분으로 구분한 아이스크림 총 주문량
상반기 동안 각 아이스크림 성분 타입과 
SELECT 
FROM 
join
성분 타입에 대한 아이스크림의
GROUP BY 
 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요.
 ORDER BY
이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.*/
SELECT b.INGREDIENT_TYPE,	sum(a.TOTAL_ORDER) as TOTAL_ORDER

from FIRST_HALF as a 
left join ICECREAM_INFO as b on a.flavor=b.flavor
group by b.INGREDIENT_TYPE
order by TOTAL_ORDER ;