--SET1: 모든 레코드 조회하기
--SELECT, FROM, ORDER_BY

SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

--SET2: 역순 정렬하기
-- DESC: 역순 정렬
ORDER BY ANIMAL_ID DESC;

--SET3: 아픈 동물 찾기
WHERE INTAKE_CONDITION = 'Sick'

--SET4: 어린 동물 찾기
WHERE INTAKE_CONDITION <> 'Aged'

--SET5: 동물의 아이디와 이름
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

--SET6: 여러 기준으로 정렬하기
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;

--SET7: 상위 n개 레코드
-- LIMIT: 출력 숫자를 제한
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;