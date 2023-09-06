-- DATE_FORMAT 사용 DATE를 각각 연월일로 나누고 다시 SALES_DATE에 저장  
select DATE_FORMAT(SALES_DATE,'%Y-%m-%d') SALES_DATE,
        PRODUCT_ID,	
        USER_ID,
        SALES_AMOUNT from ONLINE_SALE
WHERE   month(SALES_DATE) =3 

union all -- 중복되는 값이 있더라도 다 넣어서 보여달라는 의미로 ALL 사용 

select DATE_FORMAT(SALES_DATE,'%Y-%m-%d') SALES_DATE,
        PRODUCT_ID,	
         NULL,
        SALES_AMOUNT from offLINE_SALE
WHERE   month(SALES_DATE) =3 