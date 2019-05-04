### PySpark and Spark Tutorials

Following along with Jose Portilla on [Udemy Course]

### Hadoop and MapReduce
- Hadoop is method for distributing very large files across multiple machines
- uses Hadoop Distributed File System (HDFS) to allow users to work with large data sets
- Hadoop uses MapReduce to allow for computation across the distributed data set
- HDFS uses blocks of data (default 128MB) that are replicated 3 times, distributed to support fault tolerance
- smaller blocks provide more parralelization, multiple copies prevent loss of data
- MapReduce splits computational task to distributed set of files
- MapReduce consists ofJob Tracker and Task Tracker
- Job Tracker to send code to run on Task Trackers
- Task Trackers allocate CPU and Memory for the task and monitors the tasks on the worker node

### Spark
- Spark is one of latest frameworks to quickly and easily handle big data
- first released February 2013, created at Berkley
- written in Scala, so Scala normally gets the latest features
- Scala is written in Java, so Java API normally does well too!
- Python and R APIs are slowest to catch up
- flexible alternative to MapReduce - i.e. it handles splitting of computational tasks across nodes

### Spark vs MapReduce
- Hadoop and MapReduce are bound because MapReduce requires HDFS
- Spark can perform operations up to 100X faster than MapReduce
- Spark can work on HDFS, and other formats
- MapReduce writes most data to disk, while Spark keeps it in RAM and spills over to disk only when necessary. This makes Spark faster!

### Spark RDDs
- Resilient Distributed Dataset (RDD)
  - distributed collection of data
  - fault tolerant
  - parallel operation, partitioned
  - ability to use many data sources
- immutable
- lazily evaluated
- cacheable
- even if working with DataFrames, they are still RDDs under the hood

### Spark DataFrames
- Spark 2.0 shifted towards DataFrame syntax
- are now the standard way of using Spark's ML Capabilties
- [Spark Docs] are still new
- DataFrame is very familiar to Pandas DataFrames
- Columns = features
- Rows = records


### Local vs Distributed Systems
- local process is limited to computation resources on a single machine
- distributed process process has access to computational resources across a number of machines connected through a network
- after certain point, it is easier to scale out to many low cpu machnes than it is to scale up a single machine
- distributed system is fault tolerant - if one machine fails, network still runs



[Udemy Course]: https://www.udemy.com/spark-and-python-for-big-data-with-pyspark/
[Spark Docs]: http://spark.apache.org/docs/latest/