exports.loggerFormat = "dev"
exports.useErrorHandler = true
exports.enableEmailLogin = true
exports.mongodb = "mongodb://localhost/kenwiley"
exports.sessionSecret = "super duper bowls"

exports.s3Bucket = process.env.S3BUCKET || "kenwiley-mox";
exports.s3Key = process.env.S3KEY || null;
exports.s3Prefix = process.env.S3PREFIX || __dirname + "/public/";
exports.s3Secret = process.env.S3SECRET || null; 


