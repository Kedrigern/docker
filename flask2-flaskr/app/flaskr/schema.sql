-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS cislovky;

CREATE TABLE cislovky (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  en TEXT UNIQUE NOT NULL,
  cs TEXT UNIQOE NOT NULL
);

INSERT INTO cislovky (en, cs) VALUES
  ("one", "jedna"),
  ("two", "dva"),
  ("three", "tri")
;