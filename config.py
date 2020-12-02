import os

S3_BUCKET                 = os.environ.get("mybucket-face-detection-aws")
S3_KEY                    = os.environ.get("AKIAISCUUT5D3LYHOI3A")
S3_SECRET                 = os.environ.get("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")
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000