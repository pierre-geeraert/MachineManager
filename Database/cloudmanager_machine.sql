drop table IF EXISTS cloudmanager.machine;
CREATE TABLE IF NOT EXISTS cloudmanager.machine (
    id         		    integer NOT NULL PRIMARY KEY,
    namespace  	        varchar(100) NOT null,
    name              	varchar(100) NOT null,
    hour_behaviour_id 	integer      NOT null,
    day_behaviour_id  	integer      NOT null,
    replicas          	integer      NOT null
);

INSERT into cloudmanager.machine (id, namespace, name, hour_behaviour_id, day_behaviour_id,replicas) VALUES (1, 'echo', 'echo-server',  0, 1,1);
INSERT into cloudmanager.machine (id, namespace, name, hour_behaviour_id, day_behaviour_id,replicas) VALUES (2, 'wiki', 'wikijs',  1, 1,2);
INSERT into cloudmanager.machine (id, namespace, name, hour_behaviour_id, day_behaviour_id,replicas) VALUES (3, 'book', 'bookstack-db',  2, 1,1);

