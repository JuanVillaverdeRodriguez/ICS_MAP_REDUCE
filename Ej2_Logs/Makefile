1:
	hdfs dfs -put Feb95

2:
	hdfs dfs -ls

init: 1 2 

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=3 \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.map.output.key.field.separator=: \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
	-D mapreduce.partition.keycomparator.options=-k2,2nr \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	-input Feb95 -output salida_logs \
	-mapper mapper.py -reducer reducer.py \
	-file /home/cloudera/practicas/Ej2_Logs/mapper.py \
	-file /home/cloudera/practicas/Ej2_Logs/reducer.py

3m: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
	-D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=2 \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.map.output.key.field.separator=: \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	-input Feb95 -output salida_logs_mapper \
	-mapper mapper.py -file mapper.py 


4: 
	hdfs dfs -get salida_logs

4m: 
	hdfs dfs -get salida_logs_mapper

clean: 
	hdfs dfs -rm -r salida_logs
	rm -r salida_logs

cleanm: 
	hdfs dfs -rm -r salida_logs_mapper
	rm -r salida_logs_mapper

run: 3 4

runm: 3m 4m
