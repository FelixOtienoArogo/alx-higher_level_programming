-- lists all the cities of California that are in hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "Califoria")
ORDER BY id;
