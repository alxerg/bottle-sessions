# bottle-session table
CREATE TABLE tbl_bottle_session
(
	#primary id
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,

    #timestamp
    ts INT NOT NULL,

    #session id
    sid VARCHAR(255),

    #session data
    pdump BLOB,

    PRIMARY KEY (id),

    #indexes
    INDEX idx_ts (ts),
    INDEX idx_sid (sid)
);