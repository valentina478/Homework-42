import sqlite3

with sqlite3.connect('study.db') as db:
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS study(
        id_subject INTEGER,
        subject_name VARCHAR(225),
        subject_description VARCHAR(225),
        hours INTEGER,
        semester_number INTEGER
    )
    ''')

    cursor.execute('''
        INSERT INTO study VALUES
            (1, "Math", "The subject on which Math is studied", 5, 1),
            (2, "Ukrainian", "The subject on which Ukrainian is studied", 3, 2),
            (3, "Ukrainian literature", "The subject on which Ukrainian literature is studied", 2, 1),
            (4, "English", "The subject on which English is studied", 3, 2),
            (5, "History", "The subject on which History is studied", 3, 1),
            (6, "Physics", "The subject on which Physics is studied", 2, 2),
            (7, "Chemistry", "The subject on which Chemistry is studied", 2, 1),
            (8, "Geography", "The subject on which Geography is studied", 2, 2)
    ''')

    cursor.execute('''
        SELECT subject_name, semester_number
        FROM study
    ''')
    result = cursor.fetchall()
    for row in result:
        print(row)