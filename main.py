from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#create source path to read data from aws s3 bucket
S3_DATA_SOURCE_PATH = 's3://emr-wildfire-demo-12345/wildFire_Project/input/WildFireDataset_20Years.csv'
#create output path to add output in aws s3 bucket
S3_DATA_OUTPUT_PATH = 's3://emr-wildfire-demo-12345/wildFire_Project/output/'

#create main fuction to run the spark job on the EMR cluster
def main():
    #To run the spark job, create app name and include it into the EMR cluster.
    spark = SparkSession.builder.appName('WildFireDataAnalysis').getOrCreate()
    #To read the data from the aws s3 bucket.
    all_data = spark.read.csv(S3_DATA_SOURCE_PATH, header=True)
    #To give the name of the table
    all_data.createOrReplaceTempView("wildfire_dataset")
    #To write the three SQL query which will give the output on the aws s3 bucket.
    wildFire_2007_data =spark.sql("""SELECT * FROM wildfire_dataset WHERE initialdat BETWEEN '01-01-2007' AND '31-12-2007' AND area_ha > 50 LIMIT 100""")
    top_20_data = spark.sql("""SELECT * FROM wildfire_dataset ORDER BY days_between DESC LIMIT 20""")
    wildFire_2010_data =spark.sql("""SELECT * FROM wildfire_dataset WHERE initialdat BETWEEN '01-01-2010' AND '31-12-2010' AND area_ha > 50 LIMIT 100""")
    wildFire_2013_data =spark.sql("""SELECT * FROM wildfire_dataset WHERE initialdat BETWEEN '01-01-2013' AND '31-12-2013' AND area_ha > 50 LIMIT 100""")

    #To witre the sql query output into the aws s3 bucket.
    wildFire_2007_data.write.option("header", "true").mode('overwrite').csv(S3_DATA_OUTPUT_PATH)
    top_20_data.write.option("header", "true").mode("append").csv(S3_DATA_OUTPUT_PATH)
    wildFire_2010_data.write.option("header", "true").mode("append").csv(S3_DATA_OUTPUT_PATH)
    wildFire_2013_data.write.option("header", "true").mode("append").csv(S3_DATA_OUTPUT_PATH)

#function called
if __name__ == '__main__':
    main()