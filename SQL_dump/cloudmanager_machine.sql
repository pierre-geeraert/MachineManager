create table machine
(
    id                int          not null
        primary key,
    id_proxmox        int          not null,
    name              varchar(100) null,
    type              varchar(100) null,
    hour_behaviour_id int          null,
    day_behaviour_id  int          null
);

INSERT INTO cloudmanager.machine (id, id_proxmox, name, type, hour_behaviour_id, day_behaviour_id) VALUES (1, 100, 'machine_lxc_1', 'lxc', 0, 1);
INSERT INTO cloudmanager.machine (id, id_proxmox, name, type, hour_behaviour_id, day_behaviour_id) VALUES (1, 101, 'machine_qemu_1', 'qemu', 0, 1);

