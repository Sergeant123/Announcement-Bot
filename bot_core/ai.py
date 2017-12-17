"""##########################
# Imports
##########################"""
import echo.echo.py

"""##########################
# Bot Core
##########################"""
#create a function to determine which database to read from
def post_response(text):
  if echo(text): 
     message = (echo(text))
     return message

