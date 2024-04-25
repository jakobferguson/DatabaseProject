CREATE TABLE IF NOT EXISTS user (
  userID INTEGER NOT NULL,
  full_name TEXT NOT NULL,
  password TEXT NOT NULL,
  weight INTEGER,
  goal_weight INTEGER,
  goal_macros INTEGER,
  PRIMARY KEY (`userID`)
);