%default INPUT '/user/guan/test.txt';
%default OUTPUT '/user/guan/output';

-- Load the data from the file system into relation records
records = LOAD '$INPUT';

-- Split each line of text and eliminate nesting
terms = FOREACH records GENERATE FLATTEN(TOKENIZE((chararray) $0)) AS word;

-- GROUP similar terms
grouped_terms = GROUP terms BY word;

-- COUNT the number of tuples in each group
word_counts = FOREACH grouped_terms GENERATE COUNT(terms), group;

-- Store the result
STORE word_counts INTO '$OUTPUT';