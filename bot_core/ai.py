"""##########################
# Imports
##########################"""
#from echo.echo import echo_response

"""##########################
# Bot Core
##########################"""
#create a function to determine which database to read from
def post_response(text):
  message = {}
  
  if 'test' in text:
    message = "Broken I am"

  #if echo(text): 
   #  message = (echo_response(text))
  
  return message

