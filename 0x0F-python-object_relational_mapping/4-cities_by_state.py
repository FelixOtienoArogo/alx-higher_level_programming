#!/usr/bin/python3
"""lists all cities from the database htbn_0e_4_usa."""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
    FROM `cities` as `c` \
    INNER JOIN `states` as `s` \
    ON `c`.`state_id` = `s`.`id`\
    ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
