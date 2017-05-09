import java.util.*;

import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class ProcessUnits {
    public static class E_EMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private Text word;
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String lasttoken = null;
            StringTokenizer s = new StringTokenizer(line," ");
            String year = s.nextToken();

            while(s.hasMoreTokens()) {
                lasttoken=s.nextToken();
                word = new Text(year);
                int avgprice = Integer.parseInt(lasttoken);
                context.write(word, new IntWritable(avgprice));
            }
        }
    }

    public static class E_EReduce
            extends Reducer<Text, IntWritable, Text, IntWritable> {


        public void reduce(Text key, Iterable<IntWritable> values,
                           Context context
        ) throws IOException, InterruptedException {
            int maxavg = 30;
            int sum = 0;
            int count = 0;
            for (IntWritable val : values) {
                sum += val.get();
                count++;
            }
            int _result = sum/count;
            if (_result > maxavg) {
                context.write(key, new IntWritable(_result));
            }
        }
    }


    //Main function
    public static void main(String args[])throws Exception
    {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "ProcessUnits.class");

        job.setJobName("max_eletricityunits");

        job.setMapperClass(E_EMapper.class);
        job.setCombinerClass(E_EReduce.class);
        job.setReducerClass(E_EReduce.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
