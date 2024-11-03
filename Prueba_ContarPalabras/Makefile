1:
	hdfs dfs -put libros

2:
	hdfs dfs -ls

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.reduces=2 -input libros -output salida_libros -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

3Alt: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -input libros -output salida_libros -mapper mapper.py -file mapper.py 

4: 
	hdfs dfs -get salida_libros

clean: 
	hdfs dfs -rm -r salida_libros
	rm -r salida_libros

init: 1 2 3 4

run: 3 4