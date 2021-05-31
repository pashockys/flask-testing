# import sqlite3
#
# connection = sqlite3.connect('database.db')
#
#
# with open('schema.sql') as f:
#     connection.executescript(f.read())
#
# cur = connection.cursor()
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )
#
# connection.commit()
# connection.close()


import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

first_post_data = ('First Post', 'Content for the first post')
second_post_data = ('Second Post', 'Content for the second post')
all_posts = [first_post_data, second_post_data]

with connection:
    connection.executemany("INSERT INTO posts (title, content) VALUES (?, ?)", all_posts)
connection.close()