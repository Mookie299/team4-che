# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
jinja_current_directory = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
<<<<<<< HEAD
	def get(self):# for a get request
		login_template = jinja_current_directory.get_template("pages/loginPage.html")
		self.response.write(login_template.render())
		
class RecommendedPage(webapp2.RequestHandler):
	def get(self):
		recommended_template = jinja_current_directory.get_template('pages/recommendedPage.html')
		self.response.write(recommended_template.render())
=======
  def get(self):  # for a get request
	login_template=jinja_current_directory.get_template("pages/loginPage.html")
	self.response.write(login_template.render())

class QuizHandler(webapp2.RequestHandler):
  def get(self):
  	quiz_template=jinja_current_directory.get_template("pages/survey.html")
  	self.response.write(quiz_template.render())

>>>>>>> 37e0ffa906df236d95ebb5d94cb877865a5a663d


# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
<<<<<<< HEAD
  ('/recommend', RecommendedPage)
=======
  ('/quiz', QuizHandler),
>>>>>>> 37e0ffa906df236d95ebb5d94cb877865a5a663d
  ], debug=True)