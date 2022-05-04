resource "aws_s3_bucket_object" "codigo_spark_mateus" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../job_spark.py"
  etag   = filemd5("../job_spark.py")
}
#files was here