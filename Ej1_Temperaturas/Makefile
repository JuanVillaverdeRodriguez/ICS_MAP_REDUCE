1:
	hdfs dfs -put TEMPERATURAS

2:
	hdfs dfs -ls

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.reduces=2 -input TEMPERATURAS -output salida_temperaturas -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

3Alt: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -input TEMPERATURAS -output salida_temperaturas -mapper mapper.py -file mapper.py

4: 
	hdfs dfs -get salida_temperaturas

clean: 
	hdfs dfs -rm -r salida_temperaturas
	rm -r salida_temperaturas

init: 1 2 3 4

run: 3 4