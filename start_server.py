"""This script gets called by the Dockerfile in order to start up the Django server"""
# Standard library
import subprocess

command = 'python manage.py runserver 2000'
subprocess.run(command, shell=True)