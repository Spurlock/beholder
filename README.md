#What is this?

It's a very simple app with two parts: An admin UI where you select an image, and a client UI that displays that image. 

Basically it lets you choose an image, and have that image instantly (-ish) show up on however many devices.

#What's it for?

I use it when I'm running D&D games in meatspace. 

I have my laptop set up in front of me, and another screen (laptop, iPad, whatever) facing them. Then when they encounter a weird monster that I want to show them a picture of, I just click the monster's picture and suddenly they all see it on their screen.

#That's it?

Yeah. Also it's very quick-and-dirty. Nothing here should be considered suitable for any environment other than laptop localhost.

#How do I use it?

First, put some image files in the `static/` directory.

Then in the root directory, run `python beholder.py`. Assuming you're running the server and admin UI from the same machine, navigate your web browser on that machine to `localhost:8080/admin`. You should see a list of all your image files.

Then on the client machine, navigate to `whatever.that.machines.ip.address.is:8080/view`. That screen will just show whatever image the admin selected last.