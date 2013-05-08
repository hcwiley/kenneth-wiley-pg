config = require("./config")
fs = require("fs")
noxmox = require("noxmox")
path = require("path")
options =
  bucket: config.s3Bucket
  key: config.s3Key
  prefix: config.s3Prefix
  secret: config.s3Secret

if (config.s3Key?) and (config.s3Secret?)
  client = noxmox.nox.createClient(options)
else
  client = noxmox.mox.createClient(options)
exports.getS3Path = (file) ->
  url = undefined
  if config.s3Prefix and config.s3Prefix.match("http")
    return config.s3Prefix + "/" + path.join(config.s3Bucket, file)
  else
    return "/" + path.join(config.s3Bucket, file)

exports.putFile = (rel_path, type, new_name, callback) ->
  fs.readFile rel_path, (err, data) ->
    req = undefined
    return console.log(err)  if err?
    req = client.put(new_name,
      "Content-Length": data.length
      "Content-Type": type
      "x-amz-acl": "public-read"
    )
    req.on "continue", ->
      req.end data

    req.on "response", (res) ->
      res.on "data", (chunk) ->
        console.log "S3 chunk: " + chunk

      res.on "end", ->
        if res.statusCode is 200
          console.log "File stored on S3"
          callback true
        else
          callback false




exports.getFile = (file, callback) ->
  data = undefined
  req = undefined
  console.log "getting " + file
  if (config.s3Key?) and (config.s3Secret?)
    req = client.get(file)
    req.end()
    data = ""
    req.on "response", (res) ->
      chunks = undefined
      console.log "from as3: " + res.statusCode
      chunks = []
      res.on "data", (chunk) ->
        chunks.push chunk

      res.on "end", ->
        data = chunks.join("")
        console.log "got " + data.length + " from aws"
        (if typeof callback is "function" then callback(data) else undefined)


  else
    data = fs.readFile("./assets/tmp/mox/kinobi-mox/" + file, (err, data) ->
      console.log err  if err?
      (if typeof callback is "function" then callback(data) else undefined)
    )
