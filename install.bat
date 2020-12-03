@echo off
rem set http_proxy=http://proxy.wdf.sap.corp:8080
rem set https_proxy=http://proxy.wdf.sap.corp:8080
rem pip3 install venv
IF NOT EXIST env (
	echo "Install virtual environment."
	python -m venv env
	call env\Scripts\activate.bat
) else (
	echo "Skipped, virtualenv has been installed."
)
env\Scripts\pip install -r requirements.txt