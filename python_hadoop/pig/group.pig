A = LOAD 'students' AS (name:chararray, age:int, gpa:float);

R = GROUP A BY age;
ILLUSTRATE R;