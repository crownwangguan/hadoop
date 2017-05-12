REGISTER 'string_funcs.py' USING streaming_python AS string_udf;

records = LOAD 'students';

terms = FOREACH records GENERATE FLATTEN(TOKENIZE((chararray) $0)) AS word;

grouped_terms = GROUP terms BY word;

unique_terms = FOREACH grouped_terms GENERATE group as word;

term_length = FOREACH  unique_terms GENERATE word, string_udf.num_chars(word) as length;

DUMP term_length;

reverse_terms = FOREACH unique_terms GENERATE word, string_udf.reverse(word) as reverse_word;

DUMP reverse_terms;