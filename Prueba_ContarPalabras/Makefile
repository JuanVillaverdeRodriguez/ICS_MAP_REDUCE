1:
	hdfs dfs -put libros

2:
	hdfs dfs -ls

init: 1 2 

3:
	/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.reduces=2 -input libros -output salida_libros -mapper mapper.py -reducer reducer.py -file /home/cloudera/practicas/Prueba_ContarPalabras/mapper.py -file reducer.py

4: 
	hdfs dfs -get salida_libros

3m: 
	/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -input libros -output salida_libros_mapper -mapper mapper.py -file mapper.py 

4m: 
	hdfs dfs -get salida_libros_mapper

clean: 
	hdfs dfs -rm -r salida_libros
	rm -r salida_libros

cleanm:
	hdfs dfs -rm -r salida_libros_mapper
	rm -r salida_libros_mapper

run: 3 4

runm : 3m 4m
