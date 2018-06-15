import matplotlib as plt
import numpy as np
import sklearn.cluster
import sqlite3 as sql

# Connect to database
db = sql.connect("NBA.sqlite")
cursor = db.cursor()

# Load players
