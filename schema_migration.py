import sqlite3

con = sqlite3.connect('iihs.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS vehicles(id INT PRIMARY KEY, name TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS safety_categories(id INT PRIMARY KEY, name TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS scores(id INT PRIMARY KEY, name TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS vehicle_safety_category_scores(id INT PRIMARY KEY, vehicle_id INT NOT NULL, safety_category_id INT NOT NULL, score_id INT NOT NULL, FOREIGN KEY(vehicle_id) REFERENCES vehicles(id), FOREIGN KEY(safety_category_id) REFERENCES safety_categories(id), FOREIGN KEY(score_id) REFERENCES scores(id))')

