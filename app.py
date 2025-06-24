from flask import Flask, render_template,request,url_for,redirect,send_from_directory
import mysql.connector

app = Flask(__name__)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'ico.png', mimetype='image/png')


app.config['DEBUG'] = True

connection = mysql.connector.connect(
host="127.0.0.1",       
user="root",            
password="rootpass",  
database="testdb"   
) 

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/music")
def music():
    connection = mysql.connector.connect(
    host="127.0.0.1",       
    user="root",            
    password="rootpass",  
    database="testdb"   
) 
    sort = request.args.get("sort") 
    cursor = connection.cursor(dictionary=True)
    
    if sort == "year":
        cursor.execute("SELECT * FROM music ORDER BY year ASC LIMIT 40;")
    elif sort == "artist":
        cursor.execute("SELECT * FROM music ORDER BY artist ASC, year ASC LIMIT 40;")
    elif sort =="default":
        cursor.execute("SELECT * FROM music LIMIT 40;")
    elif sort =="rating":
        cursor.execute("SELECT * FROM music ORDER BY rating DESC, artist ASC LIMIT 40;")
    else:
        cursor.execute("SELECT * FROM music ORDER BY rating DESC, artist ASC LIMIT 40;")
    music_list = cursor.fetchall()
    connection.close()
    print(music_list)
    return render_template("tdowp.html", music_list=music_list)

@app.route("/artist/<artist_name>")
def artist(artist_name):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM music WHERE artist = %s order by year ASC;"
    cursor.execute(query, (artist_name,))
 
    artist_info = cursor.fetchall()

    artist_data = artist_info[0] 
    albums = [album['album'] for album in artist_info]
    img =[ img['img'] for img in artist_info]
    print(img)
    return render_template("artist.html", artist=artist_name, img = img,origin = artist_data['origin'], albums=albums,)

@app.route('/rate', methods=['POST'])
def rate():

    connection = mysql.connector.connect(
    host="127.0.0.1",       
    user="root",            
    password="rootpass",  
    database="testdb"   
    ) 
    album = request.form['music_id']
    new_rating = request.form['rating']
    
    cursor = connection.cursor(dictionary=True)
    query = "update music set rating = %s where album = %s"
    
    cursor.execute(query,(new_rating,album))
    connection.commit()

    cursor.execute("SELECT * FROM music ORDER BY rating DESC, artist ASC LIMIT 40;")
    music_list = cursor.fetchall()
    connection.close()

    return redirect(url_for('music'))

@app.route('/album', methods=['POST'])
def album():
    connection = mysql.connector.connect(
        host="127.0.0.1",       
        user="root",            
        password="rootpass",  
        database="testdb"   
    ) 
    album=request.form['music_id']
    print(album)
    cursor = connection.cursor(dictionary=True)
    query = "select * from music where img =%s"
    cursor.execute(query,(album,))
    album_data = cursor.fetchall()
    print(album_data)
    album = album_data[0]['album']
    rating = album_data[0]['rating']
    img = album_data[0]['img']
    #cursor.execute("SELECT * FROM music ORDER BY rating DESC, artist ASC LIMIT 40;")

    connection.close()
    return render_template('album.html',album = album,rating = rating, img = img)

@app.route("/artist", methods=["POST"])
def artist_redirect():
    artist_name = request.form.get("artist")
    if artist_name:
        return redirect(url_for('artist', artist_name=artist_name))
    return redirect(url_for('/'))






@app.route("/books")
def books():
    connection = mysql.connector.connect(
        host="127.0.0.1",       
        user="root",            
        password="rootpass",  
        database="testdb"   
    ) 
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute('SELECT * from books ORDER BY rating DESC, author ASC LIMIT 40;')
    book_list = cursor.fetchall()
    print(book_list)

    connection.close()
    return render_template("books.html",books_list = book_list)


if __name__ == "__main__":
    app.run(debug=True)