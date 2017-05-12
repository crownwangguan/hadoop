A = LOAD 'students' AS (name:chararray, age:int, gpa:float);

DUMP A;

STORE A INTO 'output_students' USING PigStorage('|');