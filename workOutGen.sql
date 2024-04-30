CREATE TABLE IF NOT EXISTS USER (
  userID INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL,
  pw TEXT NOT NULL,
  u_weight INTEGER,
  goal_weight INTEGER,
  goal_macros INTEGER,
);

CREATE TABLE IF NOT EXISTS EQP (
  eqp_name TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS EQP_OWNED (
  userID INTEGER,
  eqp_name TEXT, 
  PRIMARY KEY (userID, eqp_name),
  FOREIGN KEY (userID) REFERENCES USER,
  FOREIGN KEY (eqp_name) REFERENCES EQP
);

CREATE TABLE IF NOT EXISTS EXERCISE (
  exc_name TEXT PRIMARY KEY,
  instruction TEXT,
  exc_type TEXT NOT NULL,
  eqp_name TEXT,
  FOREIGN KEY (eqp_name) REFERENCES EQP
);

CREATE TABLE IF NOT EXISTS M_USED (
  exc_name TEXT,
  muscle TEXT,
  PRIMARY KEY (exc_name, muscle),
  FOREIGN KEY (exc_name) REFERENCES EXERCISE
);

CREATE TABLE IF NOT EXISTS WORKOUT (
  wid INTEGER PRIMARY KEY,
  w_name TEXT,
  w_type TEXT,
  modifiable INTEGER,
  userID INTEGER,
  FOREIGN KEY (userID) REFERENCES USER
);

CREATE TABLE IF NOT EXISTS EXC_INCLUDED (
  wid INTEGER,
  exc_name TEXT,
  exc_sets INTEGER NOT NULL,
  exc_reps INTEGER NOT NULL,
  PRIMARY KEY (wid, exc_name),
  FOREIGN KEY (wid) REFERENCES WORKOUT,
  FOREIGN KEY (exc_name) REFERENCES EXERCISE
);

CREATE TABLE IF NOT EXISTS HEALTH_LOG (
  l_timestamp TEXT,
  userID INTEGER,
  l_weight INTEGER NOT NULL,
  PRIMARY KEY (l_timestamp, userID),
  FOREIGN KEY (userID) REFERENCES USER
);

CREATE TABLE IF NOT EXISTS LIFTING_LOG (
  l_timestamp TEXT,
  userID INTEGER,
  exc_name TEXT,
  lift_weight INTEGER NOT NULL,
  lift_sets INTEGER NOT NULL,
  lift_reps INTEGER NOT NULL,
  PRIMARY KEY (l_timestamp, userID, exc_name),
  FOREIGN KEY (userID) REFERENCES USER,
  FOREIGN KEY (exc_name) REFERENCES EXERCISE
);