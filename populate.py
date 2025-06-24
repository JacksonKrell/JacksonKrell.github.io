import mysql.connector
from bs4 import BeautifulSoup
from dictionary import get_city_by_artist,artists_name_ver, get_img

connection = mysql.connector.connect(
    host="127.0.0.1",       
    user="root",            
    password="rootpass",  
    database="testdb"   
)

cursor = connection.cursor()

html_5 = """
<table class="mbgen"><tbody>
              
              <tr><td><></td><td>Boris</td><td>Flood</td><td>7</td><td></td><td>2000</td></tr>
              </tbody></table>         
"""




soup = BeautifulSoup(html_5, 'html.parser')

table_body = soup.select('table.mbgen > tbody')
rows = table_body[0].find_all('tr')
tbody = table_body[0]
rows = tbody.find_all('tr')

for row in rows:

  cells = row.find_all('td')  
  cell_data = [cell.text.strip() for cell in cells]  
  cleaned_data = [entry for entry in cell_data if len(entry) >= 3 and entry[1] and entry[2]]

  if (len(cell_data) > 1):
      
    artist = cell_data[1]
    realartist = artists_name_ver(artist)
    album = cell_data[2]
    rating = cell_data[3]
    year = cell_data[5]
    origin = get_city_by_artist(realartist)
    img = get_img(album)

    print("Artist: "+realartist+" Album: "+album+" Year: "+year+" Rating: "+rating+" Origin: "+origin+ " img: "+img)
    cursor.execute("insert into music(artist,album,year,rating,origin,img)values(%s,%s,%s,%s,%s,%s)",(realartist,album,year,rating,origin,img))
    connection.commit()

cursor.close()
connection.close()  