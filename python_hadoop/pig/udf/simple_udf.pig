REGISTER 'my_first_udf.py' USING streaming_python AS pyudfs;

A = LOAD 'students';
B = FOREACH A GENERATE pyudfs.return_one();

DUMP B;