USE market_db;
USE sys;-- 해당하는 테이블이 없으면 오류
SELECT * FROM market_db.member WHERE mem_name = '블랙핑크'; 
SELECT addr, height, debut_date FROM member; -- 순서를 바꾸어도 괜춘
SELECT addr, height 키, debut_date "데뷔 일자" FROM member; -- column뒤에 별명을 붙일 수 도 있음

SELECT * FROM member WHERE mem_number = 4; -- 해당 조건에 없는 데이터가 있을 수도 있음
SELECT mem_id, mem_name FROM member WHERE height <= 160;
SELECT mem_id, mem_name FROM member WHERE height >= 165 AND mem_number > 6; -- AND OR 모두 조건 가능
SELECT * FROM member WHERE height BETWEEN 163 AND 165; -- 기호 대신 BETWEEN을 사용해서 인덱싱 가능
SELECT * FROM member WHERE addr IN('경기','전남','경남'); -- IN()은 OR과 동일한 효과
SELECT * FROM member WHERE mem_name LIKE '우%'; -- STRING일때, %로 유추 가능
SELECT * FROM member WHERE mem_name LIKE '__핑크'; -- STRING일때, _로 유추 가능
