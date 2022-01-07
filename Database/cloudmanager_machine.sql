CREATE TABLE IF NOT EXISTS cloudmanager.machine (
    id         		integer NOT NULL PRIMARY KEY,
    id_proxmox  	integer NOT NULL,
    name              	varchar(100) null,
    type              	varchar(100) null,
    hour_behaviour_id 	integer          null,
    day_behaviour_id  	integer          null
);

INSERT into cloudmanager.machine (id, id_proxmox, name, type, hour_behaviour_id, day_behaviour_id) VALUES (1, 100, 'machine_lxc_1', 'lxc', 0, 1);
INSERT into cloudmanager.machine (id, id_proxmox, name, type, hour_behaviour_id, day_behaviour_id) VALUES (2, 101, 'machine_qemu_1', 'qemu', 0, 1);
INSERT into cloudmanager.machine (id, id_proxmox, name, type, hour_behaviour_id, day_behaviour_id) VALUES (3, 102, 'machine_qemu_2', 'qemu', 0, 1);

