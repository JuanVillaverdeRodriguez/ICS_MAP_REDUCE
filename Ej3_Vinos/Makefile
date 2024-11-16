1:
	hdfs dfs -put Vinos

2:
	hdfs dfs -ls

init: 1 2 

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=3 \
	-D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator=: \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
	-D mapred.text.key.comparator.options=-k2,2nr \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	-input Feb95 -output salida_vinos \
	-mapper mapper.py -reducer reducer.py \
	-file /home/cloudera/practicas/Ej3_Vinos/mapper.py \
	-file /home/cloudera/practicas/Ej3_Vinos/reducer.py

3m: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
	-D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=3 \
	-D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator=: \
  -D mapreduce.partition.keypartitioner.options=-k1,1 \
	-D mapred.text.key.comparator.options=-k2,2nr \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
	-input Feb95 -output salida_vinos_mapper \
	-mapper mapper.py -file mapper.py 


4: 
	hdfs dfs -get salida_vinos

4m: 
	hdfs dfs -get salida_vinos_mapper

clean: 
	hdfs dfs -rm -r salida_vinos
	rm -r salida_vinos

cleanm: 
	hdfs dfs -rm -r salida_vinos_mapper
	rm -r salida_vinos_mapper

run: 3 4

runm: 3m 4m
