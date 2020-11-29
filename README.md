# 3dPrinterFlaskAPI

### Description
Flask server that communicates with mock 3D printer flask servers: one for "Gutenberg" and one for "Xerox". Currently gets "current jobs" from both printers and the printers' nozzle temperatures, and stores this information in a redis database. 

API Documentation: 

### Setup
* Copy repository link and clone in terminal
	* `git clone https://github.com/jonahb13/3dPrinterFlaskAPI.git`
* Create virtual environment in project folder
	* `cd 3DPrinterFlaskAPI`
	* `python3 -m venv .venv`
	* `source .venv/bin/activate`
* Download required packages for the flask server
	* `pip3 install -r requirements.txt`

### Running the Server
* Open 4 separate terminal windows (all in the `3DPrinterFlaskAPI` directory)
	* In the first terminal, start the redis server
		* `redis-server`
	* In the second terminal, run the flask server for Gutenberg
		* `python3 printer_server/gutenberg.py`
	* In the third terminal, run the flask server for Xerox
		* `python3 printer_server/gutenberg.py`
	* In the fourth terminal, start the main flask app
		* `python3 main_app/app.py`
* Once the 3D Printer servers and main app server are running, run the client
	* `python3 app_client/printer_stats.py`

### Future Work
Currently, this project just mocks an interaction with 3D printer APIs/flask servers. In the future, our current code would need to be modified so that the proper printer IPs/endpoints are being used, as well as changing how information is being received/handled from the actual printers. In addition, we want to make a client webpage to display data and temperature graphs.