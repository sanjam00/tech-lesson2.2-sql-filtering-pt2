import sqlite3
import pandas as pd

conn = sqlite3.connect('pets_database.db')
# cursor = conn.cursor()

cats_data = pd.read_sql("SELECT * FROM cats;", conn)

# using comparison operators
at_least_5 = pd.read_sql("""
                         SELECT * FROM cats
                         WHERE age >= 5;
                         """, conn)

# using BETWEEN
between_age = pd.read_sql("""
                          SELECT * FROM cats
                          WHERE age BETWEEN 1 AND 3;
                          """, conn)

# NULL
no_owner = pd.read_sql("""
                       SELECT * FROM cats
                       WHERE owner_id IS NULL;
                       """, conn)

# LIKE uses wildcards to specify which parts of the string query need to be an exact match and which parts can be variable. 
# useful for querying messy data
# The most common wildcard you'll see is %. it means zero or more characters with any value can be in that position.
# could also use substring function in this case: WHERE substr(name, 1, 1) = "M", but this would return only uppercase M, rather than both upper and lower when using %
starts_with_m = pd.read_sql("""
                            SELECT * FROM cats
                            WHERE name LIKE "M%";
                            """, conn)

# LIKE with _ wildcard. means exactly one character, with any value
# For example, if we wanted to select all cats with four-letter names where the second letter was "a", we could use _a__.
second_letter_a = pd.read_sql("""
                              SELECT * FROM cats
                              WHERE name LIKE "_a__";
                              """, conn)

# COUNT: counts the number of records that meet a certain condition
# SQL aggregate functions are SQL statements that can get the average of a column's values, retrieve the minimum and maximum values from a column, 
#   sum values in a column, or count the number of records that meet certain conditions.
"""EXAMPLE: 
  SELECT COUNT(column_name)
  FROM table_name
  WHERE conditional_statement;
"""
count_owner_ids = pd.read_sql("""
                              SELECT COUNT(owner_id)
                              FROM cats
                              WHERE owner_id = 1;
                              """, conn)

# print(cats_data)
# print(at_least_5)
# print(between_age)
# print(no_owner)
# print(starts_with_m)
# print(second_letter_a)
print(count_owner_ids)

conn.close()