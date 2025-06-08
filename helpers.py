# this file has helper functions 
# each function connects to the database
# and runs sql commands

import sqlite3

def get_all_riddles():
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    # get all Questions from database
    all_riddles = conn.execute(
        """
        SELECT *
        FROM riddles
        """).fetchall()  
    
    conn.close()

    return all_riddles

def increment_row_value(column, id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    # Only allow certain columns to prevent SQL injection
    allowed_columns = ("total_guesses", "correct_guesses")
    if column not in allowed_columns:
        raise ValueError("Invalid column name")

    conn.execute(
        f"UPDATE riddles SET {column} = {column} + 1 WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()

def get_random_riddles(num_riddles):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    random_riddles = conn.execute(
        """
        SELECT * FROM riddles
         
        ORDER BY random()
        LIMIT ?""",
        (num_riddles,)
    ).fetchall()

    conn.close()

    return random_riddles

def get_random_riddles_easy(num_riddles):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    random_riddles = conn.execute(
        """
        SELECT * FROM riddles 
        WHERE difficulty = 'easy'
        ORDER BY random()
        LIMIT ?""",
        (num_riddles,)
    ).fetchall()

    conn.close()

    return random_riddles

def get_random_riddles_med(num_riddles):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    random_riddles = conn.execute(
        """
        SELECT * FROM riddles 
        WHERE difficulty = 'medium'
        ORDER BY random()
        LIMIT ?""",
        (num_riddles,)
    ).fetchall()

    conn.close()

    return random_riddles

def get_random_riddles_hard(num_riddles):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    random_riddles = conn.execute(
        """
        SELECT * FROM riddles 
        WHERE difficulty = 'hard'
        ORDER BY random()
        LIMIT ?""",
        (num_riddles,)
    ).fetchall()

    conn.close()

    return random_riddles




if __name__=="__main__":
    # -- testing helper SQL functions

    # all_riddles = get_all_riddles()
    # for riddle in all_riddles:
    #     print(riddle['id'], riddle['question'])


    increment_row_value('total_guesses', 1)

    random_riddles = get_random_riddles(3)
    for riddle in random_riddles: 
        print(riddle['id'], riddle['question'])


    
