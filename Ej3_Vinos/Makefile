1:
	hdfs dfs -put Vinos

2:
	hdfs dfs -ls

init: 1 2 

3:
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=12 \
	-input Vinos -output salida_vinos \
	-mapper mapper.py -reducer reducer.py \
	-file /home/cloudera/practicas/Ej3_Vinos/mapper.py \
	-file /home/cloudera/practicas/Ej3_Vinos/reducer.py

4: 
	hdfs dfs -get salida_vinos

5:
	cat salida_vinos/* | sort > solución.txt

run: 3 4 5

clean: 
	hdfs dfs -rm -r salida_vinos
	rm -r salida_vinos

3m: 
	sudo /usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
	-D mapreduce.job.maps=5 \
	-D mapreduce.job.reduces=12 \
	-input Vinos -output salida_vinos_mapper \
	-mapper mapper.py -file mapper.py 

4m: 
	hdfs dfs -get salida_vinos_mapper

cleanm: 
	hdfs dfs -rm -r salida_vinos_mapper
	rm -r salida_vinos_mapper

runm: 3m 4m
