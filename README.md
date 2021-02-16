1) Discuss the purpose of this database in the context of the startup, sparkify, and their analytical goals.

The data utilises the star schema to provide information about the relations, like information about the users (users table) visiting the site, information about the artist (artists table) for songs currently available, information about the songs (songs table) currently available in the sparkify streaming site, information about the time (times table) showing event time of the users on the site and finally a fact table to measure useful metrics on user preferences and business goals for the services provided by the streaming site.

Various purposes can be obtained from this database, which are information on the most preferred songs, information on users on a paid or free plain, information on daily hours of high or low traffic, information on users upgrading their plain (changing from free to page level), information on the most rated artist and information on the location for a higher demand.


2) State and justify your database schema design and ETL pipeline.

The star schema is a setup of dimension tables and fact table. The dimension table provides information on 'WHO' (who are the users), 'WHAT' (what songs are clicked), 'WHEN' (what time the song was played), 'WHICH' (which artist owns the song) and the fact table utilises these information from the dimension tables to measure useful metrics on 'HOW' (how the services are utilised and how it can be improved or optimised).The tables also utilises an upsert conflict constraint to prevent duplicate record from being inserted.This maintains the data integrity and provides an easy means to update any data.



The ETL pipeline does an extraction of data from the log files and song files generated, transforms the data to a preferable format before it is loaded into the database model. The ETL pipeline script can be synchronise to trigger/run whenever a log file is generated, i.e whenever a user lands on the site. These keeps the database updated at all time.


3) Example queries.The queries are executed on the test.ipynb folder. 

Number of free users and paid users?

%sql SELECT level, COUNT (level) FROM songplays GROUP BY level ;


What hour has the highest traffic?


%sql SELECT times.hour, COUNT (times.hour) AS hour_count FROM (songplays JOIN times ON \
                                    songplays.start_time=times.start_time)\
            GROUP BY times.hour  ORDER BY hour_count DESC LIMIT 15;
            
            
How many songs were played by each user?


%sql SELECT songplays.user_id, songplays.level, COUNT (songplays.user_id) AS user_count FROM (songplays JOIN users ON \
                           songplays.user_id=users.user_id)\
            GROUP BY songplays.user_id, songplays.level  ORDER BY user_count DESC LIMIT 15;
            
            

How many songs were played from the most played artist?


%sql SELECT songplays.artist_id, artists.artist_name, COUNT (songplays.artist_id) AS artistcount FROM (songplays JOIN       artists ON songplays.artist_id=artists.artist_id)\
            GROUP BY songplays.artist_id,artists.artist_name  ORDER BY artistcount DESC LIMIT 5;
            
            
            
            
            
NOTE: the songplay table had no match on artist_name , song title and duration, with the song and artist table. This resulted in the songplay table not having a song_id and artis_id. 