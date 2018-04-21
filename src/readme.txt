INSTALLING THE VIRTUAL ENVIRONMENT
###############################################################################
1. Create a file called "requirements.txt" with a list of every python module needed on each separate line
2. Test for virtualenv (type "virtualenv" in console)
3. If not installed: type "pip install virtualenv"
4. Type "virtualenv -p `which python` env" to create a virtual environment in the current directory
5. Type "source env/bin/activate" to activate the virtual environment
6. Type "pip install -r requirements.txt" to install all necessary modules in the virtual environment
