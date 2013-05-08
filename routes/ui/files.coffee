auth = require('./auth')
fs = require("fs")
noxmox = require("noxmox")
s3 = require('../../s3')
File = require('../../models').File

exports.upload = (req, res) ->
  auth.signIn req, res, ->
    console.log "handle upload: #{JSON.stringify req.files.file }"
    name = req.files.file.name
    name = name.replace /\ /g, '-'
    file = new File name: name
    console.log file
    path = "#{file.group}/#{file.name}"
    s3.putFile req.files.file.path, req.files.file.type, path, =>
      file.path = s3.getS3Path path
      file.save()
      console.log "s3 got next to me"
    res.redirect('/me')

exports.list = (req, res) ->
  File.find().exec (err, files)->
    if err
      console.log err
      res.send 500
    res.render "files/list", files: files, user: req.user


exports.delete = (req, res) ->
  if req.user
    File.findById(req.params.id).exec (err, file) ->
      if err
        console.log err
        res.send 500
      if !file
        console.log "didnt find the file to delete"
        res.send 500
      file.remove()
      return res.redirect("/files")
  return res.redirect("/files")
