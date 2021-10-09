
CREATE TABLE IF NOT EXISTS Users(
    user_id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    user_name TEXT NOT NULL,
    pass TEXT NOT NULL  
);

CREATE TABLE IF NOT EXISTS Lists(
    list_id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    user_id INTEGER NOT NULL,
    list_title TEXT NOT NULL,
    list_discription TEXT,
    or_list_public BOOLEAN DEFAULT 'FALSE',
    or_list_share BOOLEAN DEFAULT 'FALSE',
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS ListShares(
    list_share_id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    user_id INTEGER NOT NULL,
    list_id INTEGER NOT NULL,
    for_user1_id INTEGER,
    for_user2_id INTEGER,
    for_user3_id INTEGER,
    for_user4_id INTEGER,
    for_user5_id INTEGER,
    for_user6_id INTEGER,
    for_user7_id INTEGER,
    for_user8_id INTEGER,
    for_user9_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (list_id) REFERENCES Lists(list_id)
);

CREATE TABLE IF NOT EXISTS Posts(
    post_id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    user_id INTEGER NOT NULL,
    list_id INTEGER NOT NULL,
    latitude TEXT NOT NULL,
    longitude TEXT NOT NULL,
    place_name TEXT NOT NULL,
    post_title TEXT,
    post_discription TEXT,
    post_image BYTEA,
    post_link TEXT,
    post_date DATE,
    post_hashtag TEXT,
    or_datail BOOLEAN DEFAULT 'FALSE',
    or_post_share BOOLEAN DEFAULT 'FALSE',
    updated_time TIMESTAMP NOT NULL,
    created_time TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (list_id) REFERENCES Lists(list_id)
);

CREATE TABLE IF NOT EXISTS PostShares(
    post_share_id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    for_user1_id INTEGER,
    for_user2_id INTEGER,
    for_user3_id INTEGER,
    for_user4_id INTEGER,
    for_user5_id INTEGER,
    for_user6_id INTEGER,
    for_user7_id INTEGER,
    for_user8_id INTEGER,
    for_user9_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);