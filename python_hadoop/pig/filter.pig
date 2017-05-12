A = LOAD 'students' AS (name:chararray, age:int, gpa:float);

R = FILTER A BY age >= 20;
H = FILTER A BY (age >= 20) AND (gpa > 3.5);

DUMP R;
DUMP H;