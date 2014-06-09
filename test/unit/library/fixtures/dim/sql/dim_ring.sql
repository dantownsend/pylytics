CREATE TABLE dim_ring (
    `id` INT AUTO_INCREMENT COMMENT 'surrogate key',
    name VARCHAR(40) COMMENT 'natural key',
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                             ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) CHARSET=utf8
