

DROP TABLE IF EXISTS vid;



CREATE TABLE vid (
  vid_id TEXT PRIMARY KEY NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  publish_time TEXT,
  thumbnails TEXT
);

