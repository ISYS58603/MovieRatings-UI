# Running the movie rating Web front-end
This application shows how to call the API from a web page using simple javascript.  It doesn't exercise all the features, just a few to show how to make the call.

## Running the web front-end
To run the web front-end, you need to have a web server running.  You can use any web server you like, but we'll use the built-in Python web server for this example.

First make sure the API web server is running.  Then follow these steps:

1. Open a terminal window and navigate to the `web` directory.
2. Run the following command to start the Python web server:
   ```
   python -m http.server 8090
   ```
3. Open a web browser and navigate to `http://localhost:8090`.

Alternatively, you can use the script that is in the web directory to start the web server
1. Open a terminal window and navigate to the `web` directory.
2. Run the following command to start the Python web server:
   ```
   python web-run.py
   ```
3. Open a web browser and navigate to `http://localhost:8090`.

