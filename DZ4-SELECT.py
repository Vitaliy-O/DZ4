import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://vomar:grs12345@localhost:5432/music_site')
engine
connection = engine.connect()

# 1. название и год выхода альбомов, вышедших в 2018 году
sel1 = connection.execute("""SELECT name_album, released FROM songwriters_albums 
WHERE released = 2018;""").fetchall()
print(sel1)

# 2. название и продолжительность самого длительного трека;
sel2 = connection.execute("""SELECT track_name, duration FROM tracks
ORDER BY duration DESC
LIMIT 1;""").fetchall()
print(sel2)

# 3. название треков, продолжительность которых не менее 3,5 минуты;
sel3 = connection.execute("""SELECT track_name, duration FROM tracks 
WHERE duration >= 210;""").fetchall()
print(sel3)

# 4. названия сборников, вышедших в период с 2018 по 2020 год включительно;
sel4 = connection.execute("""SELECT name_collection, released_collection FROM collection
WHERE released_collection IN ('2018', '2019', '2020');""").fetchall()
print(sel4)

# 5. исполнители, чье имя состоит из 1 слова;
sel5 = connection.execute("""SELECT name FROM songwriter
WHERE name NOT LIKE '%% %%'

;""").fetchall()
print(sel5)
# 6. название треков, которые содержат слово "мой"/"my".
sel6 = connection.execute("""SELECT track_name FROM tracks
WHERE track_name iLIKE '%%мой%%' OR track_name iLIKE '%%my%%';""").fetchall()
print(sel6)
