import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import anvil.media



# Define the server function to process the uploaded image

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def send_pin_locs():
  rows = tables.app_tables.locations.search()
  return rows

@anvil.server.callable
def send_pictures(location):
  rows = tables.app_tables.images.search(Location=location)
  return rows

@anvil.server.callable
def send_wall_stuff():
  rows = tables.app_tables.wall.search()
  return rows

@anvil.server.callable
def sign_the_wall(name):
  # need to import datetime above!
  now = datetime.datetime.now()
  tables.app_tables.wall.add_row(Signer=name,When=now)




