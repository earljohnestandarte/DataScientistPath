import webbrowser
import os
# Display the map in a web browser
def showMap(map):
    map.save("map.html") # Create 
    filepath = os.getcwd()
    file_uri = 'file:///' + filepath + '/map.html'
    webbrowser.open_new_tab( file_uri )