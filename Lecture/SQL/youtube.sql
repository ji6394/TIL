-- 6강
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
-- 7강
USE market_db
SELECT mem_id, mem_name, debut_date
	FROM member
    ORDER BY debut_date;
SELECT mem_id, mem_name, debut_date
	FROM member
    ORDER BY debut_date DESC;
SELECT mem_id, mem_name, debut_date, height
	FROM member
    ORDER BY height DESC
    WHERE height >= 164; -- 오류 발생
SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height <= 164
    ORDER BY height DESC;
SELECT mem_id, mem_name, debut_date, height
	FROM member
    WHERE height <= 164
    ORDER BY height DESC, debut_date ASC;
SELECT *
	FROM member
    LIMIT 3;
SELECT mem_name, debut_date
	FROM member
    ORDER BY debut_date
    LIMIT 3;
SELECT mem_name, debut_date
	FROM member
    ORDER BY debut_date
    LIMIT 3,2; -- 3등과 4등 보여줌
SELECT addr FROM member;
SELECT DISTINCT addr FROM member; -- 중복된 것 제거해서 리턴
SELECT mem_id, SUM(amount) FROM buy GROUP BY mem_id;
SELECT mem_id "멤버 이름", SUM(amount) "총 구매 금액" FROM buy GROUP BY mem_id;
SELECT mem_id, SUM(price*amount) FROM buy GROUP BY mem_id;
SELECT AVG(amount) "평균 구매 횟수" FROM buy;
SELECT mem_id, AVG(amount)
	FROM buy
    GROUP BY mem_id;
SELECT COUNT(*) FROM member;
SELECT COUNT(phone1) "연락처가 있는 회원" FROM member;
SELECT mem_id "회원 아이디", SUM(price*amount)  "총 구매 금액"
	FROM buy
    WHERE SUM(price*amount) > 1000 -- 그룹 함수는 WHERE 절에 쓸 수 없음
    GROUP BY mem_id;
SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 횟수"
	FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) >1000;
SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 횟수"
	FROM buy
    GROUP BY mem_id
    HAVING SUM(price*amount) >1000
    ORDER BY SUM(price*amount) DESC;
-- 8강
USE market_db;
CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);
INSERT INTO hongong1 VALUES (1, '우디', 25);
INSERT INTO hongong1(toy_id, toy_name) VALUES (2, '버즈');
INSERT INTO hongong1(toy_name, age, toy_id) VALUES ('제시', 20, 3);
CREATE TABLE hongong2 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
INSERT INTO hongong2 VALUES(NULL, '보핍', 25);
INSERT INTO hongong2 VALUES(NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES(NULL, '렉스', 21);
SELECT * FROM hongong2;
ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL,'재남', 35);
SELECT * FROM hongong2;

CREATE TABLE hongong3 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
ALTER TABLE hongong3 AUTO_INCREMENT = 1000;
SET @@auto_increment_increment = 3;
INSERT INTO hongong3 VALUES (NULL, '토마스', 20);
INSERT INTO hongong3 VALUES(NULL, '제임스', 23);
INSERT INTO hongong3 VALUES(NULL, '고든', 25);
SELECT * FROM hongong3;
SELECT COUNT(*) FROM world.city;
DESC world.city;
SELECT * FROM world.city LIMIT 5;
CREATE TABLE city_popul ( city_name CHAR(35), population INT);
INSERT INTO city_popul
	SELECT Name, Population FROM world.city;
SELECT * FROM city_popul;
SELECT * FROM city_popul WHERE city_name = 'Seoul';
UPDATE city_popul
	SET city_name = '서울'
    WHERE city_name = 'Seoul';
SELECT * FROM city_popul WHERE city_name = '서울';
UPDATE city_popul
	SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
SELECT * FROM city_popul WHERE city_name='뉴욕';
UPDATE city_popul
	SET population = population / 10000; -- WHERE 조건없이 사용할 때에는 전체 행에 적용됨
SELECT * FROM city_popul LIMIT 5;
DELETE FROM city_popul
	WHERE city_name LIKE 'New%';