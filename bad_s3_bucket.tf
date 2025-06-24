# bad_s3_bucket.tf
resource "aws_s3_bucket" "my_insecure_bucket" {
  bucket = "my-very-insecure-devsecops-bucket-12345" # Must be globally unique

  # BAD: No server-side encryption defined
  # BAD: No public access block defined, potentially allowing public access
  # BAD: No versioning or logging (though Checkov might not flag these as critical security issues directly)
}

resource "aws_s3_bucket_acl" "my_insecure_bucket_acl" {
  bucket = aws_s3_bucket.my_insecure_bucket.id
  acl    = "public-read" # BAD: Explicitly setting public-read ACL
}

resource "aws_s3_bucket_public_access_block" "my_s3_block" {
  bucket = aws_s3_bucket.my_insecure_bucket.id

  # BAD: Setting these to false to allow public access.
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
