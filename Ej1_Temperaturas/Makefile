1:
	hdfs dfs -put TEMPERATURAS

2:
	hdfs dfs -ls

init: 1 2 

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator=: \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.text.key.comparator.options=-k2,2nr \
	-D mapreduce.job.reduces=3 \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	-input TEMPERATURAS -output salida_temperaturas \
	-mapper mapper.py -reducer reducer.py \
	-file /home/cloudera/practicas/Ej1_Temperaturas/mapper.py \
	-file /home/cloudera/practicas/Ej1_Temperaturas/reducer.py

3m: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
	-D stream.map.output.field.separator=: \
  -D stream.num.map.output.key.fields=2 \
  -D map.output.key.field.separator=: \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.text.key.comparator.options=-k2,2nr \
  -D mapreduce.partition.keypartitioner.options=-k1 \
	-input TEMPERATURAS -output salida_temperaturas_mapper \
	-mapper mapper.py -file mapper.py 


4: 
	hdfs dfs -get salida_temperaturas

4m: 
	hdfs dfs -get salida_temperaturas_mapper

clean: 
	hdfs dfs -rm -r salida_temperaturas
	rm -r salida_temperaturas

cleanm: 
	hdfs dfs -rm -r salida_temperaturas_mapper
	rm -r salida_temperaturas_mapper

run: clean 3 4

runm: cleanm 3m 4m
