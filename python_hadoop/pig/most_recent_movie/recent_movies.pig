REGISTER 'movies_udf.py' USING streaming_python AS movies_udf;

-- Load the data frmo the file system
records = LOAD 'movies.csv' USING PigStorage(',') AS (id: int, title:chararray, release_date:chararray);

-- Parse the titles and determine how many days since the release date
titles = FOREACH records GENERATE movies_udf.parse_title(title), movies_udf.days_since_release(title);

-- Order the movies by te time since release
most_recent = ORDER titles BY days_since_release ASC;

-- Get the ten most recent movies
top_ten = LIMIT most_recent 10;

-- Display the top ten most recent movies
DUMP top_ten;
