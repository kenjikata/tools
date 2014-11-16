# -*- coding: utf-8 -*-
import pyodbc
import codecs
import sys
import calendar
import datetime

filename = "count.txt"
f = codecs.open(filename,'w',"utf-8")

def write(rows,date):
		for row in rows:
			f.write(date+","+str(row[0])+"\r\n")
			#f.write(row[1])

def fileend():
	try:
		f.close()
	except (pyodbc.Error) as e:
		print (e.args[1])

def main():
	try:
		# Windows認証
		cnn = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server Native client 11.0}',server = 'localhost', database = ‘###DATABASE_NAME###’)
		cur = cnn.cursor()

		# 年ループ
		for year in range(2000,2010):
			# 月ループ
			for month in range(1, 13):
				#月末日を取得
				days = calendar.monthrange(year, month)
				# 日ループ
				for day in range(1,days[1]+1):
					#文字列連結
					st_date = str(year) + "-" + "%02d" % (month) + "-" + "%02d" % (day) + " 15:00:00"
					#文字列→datetime
					start_dt = datetime.datetime.strptime(st_date, '%Y-%m-%d %H:%M:%S')
					end_dt = start_dt + datetime.timedelta(days=+1)

					# SQL実行
					cur.execute("""SELECT count(*) FROM ###TABLE_NAME### WHERE ###COLUMN_NAME### is not null and ###COLUMN_NAME### >= '%s' and ###COLUMN_NAME### < '%s'""" % (start_dt,end_dt))
					rows = cur.fetchall()
					date = str(year) + "%02d" % (month) + "%02d" % (day)
					write(rows,date)

		cur.close()
		cnn.close()

	except (pyodbc.Error) as e:
		print (e.args[1])

if __name__ == '__main__':
	main()
	fileend()
