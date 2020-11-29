# 3dPrinterFlaskAPI

### Description
Flask server that exposes information from multiple endpoints in mock 3D printer flask servers: one server called "Gutenberg" and one called "Xerox". Collector communicates with "Gutenberg" and "Xerox" to get their current print job and the nozzle temperatures, and stores this information in a redis database. Current endpoints on the Flask server are '/current_job' and '/nozzle_temps'.

### Setup
* Copy repository link and clone in terminal
	* `git clone https://github.com/jonahb13/3dPrinterFlaskAPI.git`
* Create virtual environment in project folder
	* `cd 3DPrinterFlaskAPI`
	* `python3 -m venv .venv`
	* `source .venv/bin/activate`
* Download required packages for the flask server
	* `pip3 install -r requirements.txt`

### Running the Servers
* Open 5 separate terminal windows (all in the `3DPrinterFlaskAPI` directory)
	* In the first terminal, start the redis server
		* `redis-server`
	* In the second terminal, run the flask server for Gutenberg
		* `python3 printer_server/gutenberg_app.py`
	* In the third terminal, run the flask server for Xerox
		* `python3 printer_server/xerox_app.py`
	* In the fourth terminal, start the main flask app
		* `python3 main_app/app.py`
* Once the 3D Printer servers and main app server are running, run the client in the fifth terminal 
	* `python3 app_client/printer_stats.py`

### Future Work
Currently, this project just mocks an interaction with 3D printer APIs/flask servers. In the future, our current code would need to be modified so that the proper printer IPs/endpoints are being used, as well as changing how information is being received/handled from the actual printers. In addition, we want to make a client webpage to display data and temperature graphs.