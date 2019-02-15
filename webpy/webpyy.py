import web
	#导入web.py模块
render = web.template.render('templates/')

urls = (
	'/(.*)', 'index'
)

class index:
	def GET(self, name):
		return render.halo(name)


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

