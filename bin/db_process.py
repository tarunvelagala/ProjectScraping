import psycopg2
import sys
import urlparse



def writeDB(username, make, model, year, email):
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con=None
	try:
		con=psycopg2.connect(database='subscribe', user='administrator')
		cur=con.cursor()
		cur.execute("INSERT INTO users VALUES ('" + username + "','" + make + "','" + model + "','" + year + "','" + email + "')")
		con.commit()
		
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)
    
	finally:
		if con:
		    con.close()
    
