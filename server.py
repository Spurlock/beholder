import web
import os


class Image(object):

    # Retrieve the currently active image
    def GET(self):
        img_filename = ""
        with open('db.txt', 'r') as file:
            img_filename = file.read()
        return "static/" + img_filename


class Admin(object):
    # Set the active image
    def POST(self):
        filename = web.input()['filename']
        with open("db.txt", 'w') as file:
            file.write(filename)

    # Render the admin UI
    def GET(self):
        files = []
        for _, _, filenames in os.walk("static"):
            files.extend(filenames)
            break

        render = web.template.render('templates')
        return render.admin(files=files)


class View(object):
    # Render the image viewer client
    def GET(self):
        render = web.template.render('templates')
        return render.view()


urls = (
    '/admin', Admin,
    '/view', View,
    '/image', Image
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
