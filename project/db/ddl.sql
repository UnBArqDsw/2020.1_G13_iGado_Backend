CREATE TABLE _USER(
    id_user SERIAL NOT NULL,
    email VARCHAR(50) NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    is_proprietary BOOLEAN NOT NULL,
    CONSTRAINT _USER_PK PRIMARY KEY (id_user)
);

CREATE TABLE FARM (
    id_farm SERIAL NOT NULL,
    size_farm INT NOT NULL,
    CONSTRAINT FARM_PK PRIMARY KEY (id_farm),
    CONSTRAINT FARM_USER_FK FOREIGN KEY (id_user)
        REFERENCES _USER(id_user)
);

CREATE TABLE work (
    id_user INT NOT NULL,
    id_farm INT NOT NULL,
    CONSTRAINT work_PK PRIMARY KEY (id_user, id_farm),
    CONSTRAINT work_USER_FK FOREIGN KEY (id_user)
        REFERENCES _USER(id_user),
    CONSTRAINT work_FARM_FK FOREIGN KEY (id_farm)
        REFERENCES FARM(id_farm)
);