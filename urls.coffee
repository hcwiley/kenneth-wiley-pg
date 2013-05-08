config = require("./config")
routes = require('./routes')

module.exports = (app) ->

  app.post "/auth/email", routes.ui.auth.email
  
  app.get "/auth/success", routes.ui.auth.success
  app.get "/auth/failure", routes.ui.auth.failure
  app.get "/auth/logout", routes.ui.auth.logout
  
  app.put "/me", routes.ui.me.update
  
  # UI routes
  app.get "/", (req, res) ->
    res.render "index.jade",
      title: "Studio Time"
  
  # you need to be signed for this business!
  #app.all "*", routes.ui.auth.signIn
  
  app.get "/me", routes.ui.me.show
  
  app.post "/upload", routes.ui.files.upload
  app.get "/files", routes.ui.files.list
  app.delete "/files/:id", routes.ui.files.delete
