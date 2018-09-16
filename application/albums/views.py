from application import app, db
from flask import redirect, render_template, request, url_for
from application.albums.models import Album

@app.route("/albums", methods=["GET"])
def albums_index():
    return render_template("albums/list.html", albums = Album.query.all())

@app.route("/albums/new/")
def albums_form():
    return render_template("albums/new.html")

@app.route("/albums/change/<album_id>/", methods=["POST"])
def album_change_details(album_id):

    return render_template("albums/change.html", album = Album.query.get(album_id))

@app.route("/albums/<album_id>/", methods=["POST"])
def albums_change_details(album_id):

    t = Album.query.get(album_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("albums_index"))    

@app.route("/albums/", methods=["POST"])
def albums_create():
    t = Album(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("albums_index"))