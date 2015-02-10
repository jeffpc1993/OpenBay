import web
import scraper
render = web.template.render('templates/')
urls = (
	'/', 'index',
	'/next/seed/(.*)','seed',
	#'/last/seed/(.*)','seed',	
	'/next/(.+)','next',
	'/first','index',
	'/seed/(.*)','seed',
	#'/last/(.+)','last',
	
	
		
)
db= web.database(dbn='mysql',user='root',pw='jeffpc1234',db='torrents')

class index:

	def GET(self):
		num=1
		todos=db.select('testcsv',limit=20)
        	return render.index(todos,num)
class seed:
	def GET(self,has):
		thedict=scraper.scrape('udp://open.demonii.com:1337/',[has])
		arr=thedict.values()
		dic=arr[0]
		seeds=dic['seeds']
		peers=dic['peers']
		complete=dic['complete']
		return render.seed(seeds,peers,complete)
class next:
	def GET(self,num):
		number=int(num)
		todos=db.select('testcsv',limit=20,offset=20*number)
		number=number+1
        	return render.next(todos,number)
		

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
