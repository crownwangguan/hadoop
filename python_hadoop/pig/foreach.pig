A = LOAD 'students' AS (name:chararray, age:int, gpa:float);

R = FOREACH A GENERATE *;
DUMP R;