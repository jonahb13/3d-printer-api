# 3dPrinterFlaskAPI

### Description
___
Flask server that communicates with Moravian College's 3D printers, Gutenberg and Xerox. Currently gets both printer's print job history from their respective API's and stores the data in a redis database.

### Setup
___
* Copy repository link and clone in terminal
	* `git clone https://github.com/jonahb13/3dPrinterFlaskAPI.git`
* Create virtual environment in project folder
	* `cd 3DPrinterFlaskAPI`
	* `python3 -m venv .venv`
	* `source .venv/bin/activate`
* Download required packages for the flask server
	* `pip install -r requirements.txt`

### Running the Server
___
* Open 2 separate terminal windows 
	* In the first terminal, start the redis server
		* `redis-server`
	* In the second terminal, run the flask server
		* `python3 app.py`

### Future Work
___
