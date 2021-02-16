# DROP TABLES


songplay_table_drop = "DROP TABLE IF EXISTS songplays "
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"
    

# CREATE TABLES

try:    
    songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int NOT NULL,
                            start_time int NOT NULL,user_id  int NOT NULL,level VARCHAR,song_id VARCHAR,
                            artist_id VARCHAR,session_id INT,location TEXT,user_agent TEXT,
                            PRIMARY KEY (songplay_id))""")
except Exception as e:
    print("unable to create songplays")
    print(e)

try:
    user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL,first_name VARCHAR,last_name VARCHAR,\
                        gender CHAR(1),level VARCHAR, PRIMARY KEY (user_id ))
                        """)
except Exception as e:
    print("unable to create users")
    print(e)
    

try:
    song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR NOT NULL,title TEXT,\
                        artist_id VARCHAR NOT NULL,\
                        year BIGINT,duration NUMERIC, PRIMARY KEY (song_id))
                        """)
except Exception as e:
    print("unable to create songs")
    print(e)
    

try:
    artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR,artist_name TEXT,\
                         location VARCHAR,latitude NUMERIC,longitude NUMERIC, PRIMARY KEY (artist_id))
                        """)

except Exception as e:
    print("unable to create artists")
    print(e)
    
try:
    
    time_table_create = ("""CREATE TABLE IF NOT EXISTS times (start_time int NOT NULL,hour int,day int,\
                    week int,month int,year int,weekday VARCHAR, PRIMARY KEY (start_time))""")
except Exception as e:
    print("unable to create times")
    print(e)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,\
                            artist_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)\
                            ON CONFLICT (songplay_id) 
                            DO NOTHING
                            """)

user_table_insert = ("""INSERT INTO users (user_id,first_name,last_name,gender,level)\
                        VALUES (%s,%s,%s,%s,%s)\
                        ON CONFLICT (user_id) 
                        DO NOTHING
                        """)

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration) VALUES (%s,%s,%s,%s,%s)\
                        ON CONFLICT (song_id) 
                        DO NOTHING 
                        """)

artist_table_insert=("""INSERT INTO artists (artist_id,artist_name,location,latitude,longitude) VALUES (%s,%s,%s,%s,%s)\
                        ON CONFLICT (artist_id) 
                        DO NOTHING
                        """)


time_table_insert = ("""INSERT INTO times (start_time,hour,day,week,month,year,weekday) VALUES (%s,%s,%s,%s,%s,%s,%s)\
                        ON CONFLICT (start_time) 
                        DO NOTHING
                    """)

# FIND SONGS

song_select = ("""SELECT songs.song_id ,artists.artist_id FROM (songs JOIN artists ON songs.artist_id=artists.artist_id)\
                   WHERE (songs.title,artists.artist_name,songs.duration) IN ( VALUES (%s,%s,%s))""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,song_table_create,time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# WHERE title = '%s' AND artist_name = '%s' AND duration = '%s' songs.title,