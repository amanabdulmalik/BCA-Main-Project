

def connection():
	import pymysql
	connect = pymysql.connect(host='localhost',user='root',passwd='',db='crime_scene_detection',port=3306)
	cursor = connect.cursor()
	return connect, cursor