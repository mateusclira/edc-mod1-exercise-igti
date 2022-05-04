# HCL - Hashicorp configuration Language
# Linguagem declarativa

resource "aws_s3_bucket" "dl" {
  #parametros
  bucket = "datalake-mateus-igti-edc-tf"
  acl    = "private"

  server_side_encryption_configuration {

    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}
/*
*/