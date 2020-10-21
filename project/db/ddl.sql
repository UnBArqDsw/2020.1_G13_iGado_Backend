CREATE TABLE _USER(
    user_id SERIAL NOT NULL,
    email VARCHAR(50) NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_proprietary BOOLEAN NOT NULL,
    CONSTRAINT _USER_PK PRIMARY KEY (user_id)
);

CREATE TABLE FARM (
    farm_id SERIAL NOT NULL,
    farm_name VARCHAR(100) NOT NULL,
    size_farm INT NOT NULL,
    CONSTRAINT FARM_PK PRIMARY KEY (farm_id)
);

CREATE TABLE work (
    user_id INT NOT NULL,
    farm_id INT NOT NULL,
    CONSTRAINT work_PK PRIMARY KEY (user_id, farm_id),
    CONSTRAINT work_USER_FK FOREIGN KEY (user_id)
        REFERENCES _USER(user_id),
    CONSTRAINT work_FARM_FK FOREIGN KEY (farm_id)
        REFERENCES FARM(farm_id)
);