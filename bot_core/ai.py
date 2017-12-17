"""##########################
# Imports
##########################"""
from echo.echo import echo_response

"""##########################
# Bot Core
##########################"""
#create a function to determine which database to read from
def post_response(text):
  if echo(text): 
     message = (echo_response(text))
     return message

