# Wildfire Big Data Analytics Project

## Introduction

This project aims to analyze wildfire Bigdata using AWS services, particularly Amazon S3, Amazon EMR (Elastic MapReduce), and AWS EC2 (Elastic Compute Cloud). The analysis is performed using PySpark SQL libraries on Apache Spark.

## Technologies Used

- **AWS S3**: Used to store the raw wildfire data before processing.
- **AWS EMR**: Utilized for distributed processing of the data using Apache Spark.
- **AWS EC2**: Used as the computing resource for running PySpark.
- **PySpark SQL Libraries**: Used for querying and analyzing the data.
- **Apache Spark**: Framework for distributed data processing.
- **HTML/CSS**: Used for build simple website to display outputs.

## Project Workflow

1. **Data Collection**: Initially, wildfire data is collected from reliable sources. For this project, approximately 2 GB of wildfire data was collected.

2. **Data Uploading to S3**: The collected wildfire data is uploaded to an AWS S3 bucket for storage and easy access.

3. **Data Processing on EMR**: AWS EMR is used to distribute the data processing tasks across multiple nodes. The data is distributed on 2 core nodes and one master node for efficient processing.

4. **Data Analysis with PySpark**: PySpark SQL libraries are utilized to run SQL queries on the distributed dataset. This enables us to analyze the large dataset efficiently.

5. **Results Storage in S3**: The results of the data analysis are stored back in the AWS S3 bucket for easy access and further processing if needed.

6. **Website Display**: Finally, the results are displayed on a simple HTML/CSS website. The website fetches the analyzed data from the S3 bucket and presents it in a user-friendly format.

## References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
