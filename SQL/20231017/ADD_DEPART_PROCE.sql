-- DEPART 테이블의 데이터 추가 수행하는 프로시저 작성
CREATE OR REPLACE PROCEDURE ADD_DEPART
(
    INPUT_NUM IN VARCHAR2,
    INPUT_NAME IN VARCHAR2
)
IS BEGIN
    INSERT INTO DEPART VALUES(INPUT_NUM, INPUT_NAME);
END ADD_DEPART;
