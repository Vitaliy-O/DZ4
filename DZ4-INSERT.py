import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://vomar:grs12345@localhost:5432/music_site')
engine
connection = engine.connect()

# АЛЬБОМЫ
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(1, 'Звезда по имени Солнце', 1989)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(2, 'Vip Mix', 2008)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(3, 'Громче воды, выше травы', 2002)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(4, 'Группа крови', 1988)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(5, 'Горизонт событий', 2017)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(6, 'Хентай', 2018)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(7, 'Эгоист', 2017)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(8, 'Баста 40', 2020)""");
connection.execute("""INSERT INTO   songwriters_albums(id, name_album, released) VALUES(9, 'Жиган лимон', 1993)""");

# ИСПОЛНИТЕЛИ
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(1, 'Гр. Кино')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(2, 'DJ Romeo')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(3, 'Каста')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(4, 'Би-2')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(5, 'Niletto')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(6, 'Дима Билан')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(7, 'Баста')""");
connection.execute("""INSERT INTO   songwriter(id, name) VALUES(8, 'Михаил Круг')""");

# Связующая таблица АЛЬБОМОВ и ИСПОЛНИТЕЛЕЙ
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(1, 1, 1)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(2, 2, 2)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(3, 3, 3)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(4, 1, 4)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(5, 5, 6)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(6, 6, 7)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(7, 7, 8)""");
connection.execute("""INSERT INTO   joint_album(id, id_sw, id_album) VALUES(8, 8, 9)""");

# ЖАНРЫ
connection.execute("""INSERT INTO   genre(id, genre_name) VALUES(1, 'Поп')""");
connection.execute("""INSERT INTO   genre(id, genre_name) VALUES(2, 'Рок')""");
connection.execute("""INSERT INTO   genre(id, genre_name) VALUES(3, 'Рэп')""");
connection.execute("""INSERT INTO   genre(id, genre_name) VALUES(4, 'Шансон')""");
connection.execute("""INSERT INTO   genre(id, genre_name) VALUES(5, 'Электронная')""");

# Связующая таблица ЖАНРОВ и ИСПОЛНИТЕЛЕЙ
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(1, 1, 2)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(2, 2, 5)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(3, 3, 3)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(4, 4, 2)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(5, 5, 1)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(6, 6, 1)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(7, 7, 3)""")
connection.execute("""INSERT INTO   sw_genres(id, id_sw, id_genre) VALUES(8, 8, 4)""")

# гр. Кино - Звезда по имени Солнце
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(1, 1, 'Песня без слов', 307)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(2, 1, 'Звезда по имени Солнце', 226)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(3, 1, 'Невесёлая песня', 258)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(4, 1, 'Сказка', 359)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(5, 1, 'Место для шага вперёд', 220)""")

# DJ Romeo - Vip Mix
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(6, 2, 'The Way', 435)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(7, 2, 'Sunrise', 501)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(8, 2, 'Luna', 395)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(9, 2, 'Улетели навсегда', 401)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(10, 2, 'Passion(My way)', 375)""")

# Каста - Громче воды, выше травы
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(11, 3, 'Но пацанам из Касты…', 27)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(12, 3, 'Куда надо смотреть', 222)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(13, 3, 'На порядок выше', 238)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(14, 3, 'Про Макса', 205)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(15, 3, 'Язычество', 304)""")

# гр. Кино - Группа крови
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(16, 4, 'Группа крови', 287)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(17, 4, 'Закрой за мной дверь, я ухожу', 257)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(18, 4, 'Война', 245)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(19, 4, 'Спокойная ночь', 368)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(20, 4, 'Дальше действовать будем мы', 237)""")

# БИ-2 - Горизонт событий
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(21, 5, 'Лётчик', 351)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(22, 5, 'Чёрное солнце', 289)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(23, 5, 'Тема века', 218)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(24, 5, 'Детство', 194)""")
connection.execute("""INSERT INTO   tracks(id, id_album, track_name, duration) VALUES(25, 5, 'Лайки', 211)""")

# Niletto - Хентай
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(26, 6, 'Угольки', 171)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(27, 6, 'Шапка', 217)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(28, 6, 'Сеньора', 192)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(29, 6, 'Эвтаназия души', 80)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(30, 6, 'Хентай', 227)""")

# Дима Билан - Эгоист
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(31, 7, 'Эгоист', 246)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(32, 7, 'Держи', 220)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(33, 7, 'Атом', 190)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(34, 7, 'Прости', 222)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(35, 7, 'Рай', 224)""")

# Баста - Баста 40
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(36, 8, 'Интро', 145)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(37, 8, 'С самых низов', 339)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(38, 8, 'Дочь огня', 249)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(39, 8, 'Баста 40', 334)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(40, 8, 'Лампочка', 390)""")

# Михаил Круг - Жиган лимон
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(41, 9, 'Электричка', 186)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(42, 9, 'Девочка-пай', 257)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(43, 9, 'Кольщик', 287)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(44, 9, 'Дороги', 279)""")
connection.execute("""INSERT INTO tracks(id, id_album, track_name, duration) VALUES(45, 9, 'Жиган-лимон', 173)""")


# Сборник №1
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(1, 'Легенды русского рока', 2000)""")
# Сборник №2
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(2, 'Сборник российской поп-музыки', 2020)""")
# Сборник №3
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(3, 'Сборник рэпа', 2021)""")
# Сборник №4
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(4, 'Рок & Шансон', 2019)""")
# Сборник №5
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(5, 'Dance', 2018)""")
# Сборник №6
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(6, 'Мой сборник-2021', 2021)""")
# Сборник №7
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(7, 'Сборник в дорогу', 2020)""")
# Сборник №8
connection.execute("""INSERT INTO collection(id, name_collection, released_collection) VALUES(8, 'Рок & Билан', 2019)""")

# Сборник №1 из 9 песен 'Легенды русского рока', 2000
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(1, 1, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(2, 2, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(3, 3, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(4, 16, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(5, 17, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(6, 19, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(7, 21, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(8, 22, 1)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(9, 25, 1)""")

# Сборник №2 из 6 песен 'Сборник российской поп-музыки', 2020
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(10, 26, 2)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(11, 27, 2)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(12, 30, 2)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(13, 31, 2)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(14, 33, 2)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(15, 35, 2)""")

# Сборник №3 из 6 песен 'Сборник рэпа', 2021
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(16, 37, 3)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(17, 38, 3)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(18, 39, 3)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(19, 12, 3)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(20, 14, 3)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(21, 11, 3)""")

# Сборник №4 из 7 песен 'Рок & Шансон', 2019
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(22, 21, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(23, 22, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(24, 25, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(25, 2, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(26, 5, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(27, 43, 4)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(28, 45, 4)""")

# Сборник №5 из 4 песен 'Dance', 2018
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(29, 7, 5)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(30, 10, 5)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(31, 28, 5)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(32, 30, 5)""")

# Сборник №6 из 3 песен 'Мой сборник-2021', 2021
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(33, 13, 6)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(34, 33, 6)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(35, 44, 6)""")

# Сборник №7 из 6 песен
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(36, 8, 7)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(37, 9, 7)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(38, 32, 7)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(39, 34, 7)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(40, 22, 7)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(41, 25, 7)""")

# Сборник №8 из 9 песен
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(42, 13, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(43, 11, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(44, 15, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(45, 16, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(46, 18, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(47, 19, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(48, 34, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(49, 31, 8)""")
connection.execute("""INSERT INTO tc_sa(id, tracks_id, collection_id) VALUES(50, 35, 8)""")


ins_songwriters_albums = connection.execute("""SELECT * FROM songwriters_albums""").fetchall()
print(ins_songwriters_albums)
ins_songwriter = connection.execute("""SELECT * FROM songwriter""").fetchall()
print(ins_songwriter)
ins_joint_album = connection.execute("""SELECT * FROM joint_album""").fetchall()
print(ins_joint_album)
ins_genre = connection.execute("""SELECT * FROM genre""").fetchall()
print(ins_genre)
ins_sw_genre = connection.execute("""SELECT * FROM sw_genres""").fetchall()
print(ins_sw_genre)
ins_tracks = connection.execute("""SELECT * FROM tracks""").fetchall()
print(ins_tracks)
ins_collection = connection.execute("""SELECT * FROM collection""").fetchall()
print(ins_collection)
ins_tc_sa = connection.execute("""SELECT * FROM tc_sa""").fetchall()
print(ins_tc_sa)