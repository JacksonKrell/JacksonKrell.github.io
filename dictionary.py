artists_by_city = {
    "Nogales":["Charles Mingus"],
    "Lubbock":["Buddy Holly"],
    "New York":["Buddy Rich","New York Philharmonic","Sonny Rollins"],
    "Newport News":["Ella Fitzgerald"],
    "Washington":["Duke Ellington"],
    "Alton":["Miles Davis"],
    "別府市":['秋吉敏子'],
    "Tampa" : ["Cannonball Adderley"],
    "Hamlet" : ["John Coltrane"],
    "Yale": ["Chet Baker"],
    "Jamestown":["Peggy Lee"],
    "Philadelphia":["Billie Holiday"],
    "Macon":["Little Richard"],
    "Hoboken":["Frank Sinatra"],
    "Tryon":["Nina Simone"],
    "Viper":["Jean Ritchie"],
    "Vernon":["Roy Orbison"],
    "Glendale": ["Marty Robbins"],
    "Tupelo":["Elvis Presley"],
    "Kansas City":['Charlie Parker'],
    "Rocky Mount":["Thelonious Monk"],
    "東京":['フィッシュマンズ','ボリス'],
    'Ruston':['Neutral Milk Hotel'],
    'Rockville':['Father John Misty'],
    'Orlando':['Death'],
    'Montréal ':['Godspeed You! Black Emperor'],
    'Baltimore':['Animal Collective'],
    'Portland':['Elliott Smith'],
    "London":['Yes','Pink Floyd'],
}

artists_by_name = {
    "Charles Mingus":["Mingus"],
    "New York Philharmonic":["New York Philharmonic / Leonard Bernstein"],
    "Buddy Rich":["Gene Krupa & Buddy Rich"],
    "Duke Ellington":["Duke Ellington and His Orchestra"],
    "Ella Fitzgerald": ["Ella Fitzgerald & Louis Armstrong"],
    "秋吉敏子":["Toshiko Akiyoshi"],
    "Thelonious Monk":["Thelonious Monk Septet"],
    "フィッシュマンズ":["Fishmans"],
    "Godspeed You! Black Emperor":["Godspeed You Black Emperor!"],
    'Animal Collective':['Avey Tare and Panda Bear'],
    'ボリス':['Boris']

}

img_dictionary = {
    "RAM.jpg": ["'Round About Midnight"],
    "KoB.jpg": ["Kind of Blue"],
    "SE.jpg": ["Somethin' Else"],
    "TA.jpg": ["Toshiko's Piano"],
    "CBS.jpg" :['Chet Baker Sings'],
    "GS.jpg" :['Giant Steps'],
    'BT.jpg' :['Blue Train'],
    'MAU.jpg' :['Mingus Ah Um'],
    'SC.jpg':['Saxophone Colossus'],
    'SFDL.jpg':['Songs for Distingué Lovers'],
    'EU.jpg':['Ellington Uptown'],
    'GBATS.jpg':['Gunfighter Ballads and Trail Songs'],
    'LSDP.jpg':['Le sacre du printemps'],
    'EAL.jpg':['Ella and Louis'],
    'CPWS.jpg':['Charlie Parker With Strings'],
    'ID.jpg':['In Dreams'],
    'EP.jpg':['Elvis Presley'],
    'STTSOHKMF.jpg':['Singing the Traditional Songs of Her Kentucky Mountain Family'],
    'ITWSH.jpg':['In the Wee Small Hours'],
    'SFSL.jpg':['Songs for Swingin\' Lovers!'],
    'BH.jpg':['Buddy Holly'],
    'HLR.jpg':['Here\'s Little Richard'],
    'BCWPL.jpg':['Black Coffee With Peggy Lee'],
    'MM.jpg':['Monk\'s Music'],
    'LGB.jpg':['Little Girl Blue'],
    'KaR.jpg':['Krupa and Rich'],
    'LS.jpg':['LONG SEASON'],
    'ITAOTS.jpg':["In the Aeroplane Over the Sea"],
    'PC.jpg':['Pure Comedy'],
    'DS.png':['Symbolic'],
    'UNS.jpg':['宇宙 日本 世田谷'],
    'LYSF.jpg':['Lift Your Skinny Fists Like Antennas to Heaven!'],
    'STGSTV.jpg':["Spirit They\'re Gone Spirit They\'ve Vanished"],
    'E-O.png':['Either/Or'],
    'CttE.png':['Close to the Edge'],
    'A.png':['Animals'],
    'KU.png':['空中キャンプ'],
    'BPK.jpg':['Pink'],
    'bf.png':['Flood'],
}

def get_city_by_artist(artist_name):
    for city, artists in artists_by_city.items():
        if artist_name in artists:
            return city
    return "No City"

def artists_name_ver(artist_name):
    for artist, name in artists_by_name.items():
        if artist_name in name:
            return artist
    return artist_name

def get_img(artist_name):
    for img, artist in img_dictionary.items():
        if artist_name in artist:
            return img
    return "No img.jpg"

