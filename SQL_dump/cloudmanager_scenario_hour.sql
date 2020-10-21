create table scenario_hour
(
    id_scenario   int          not null
        primary key,
    name_scenario varchar(255) null,
    state_at_0    binary(1)    null,
    state_at_1    binary(1)    null,
    state_at_2    binary(1)    null,
    state_at_3    binary(1)    null,
    state_at_4    binary(1)    null,
    state_at_5    binary(1)    null,
    state_at_6    binary(1)    null,
    state_at_7    binary(1)    null,
    state_at_8    binary(1)    null,
    state_at_9    binary(1)    null,
    state_at_10   binary(1)    null,
    state_at_11   binary(1)    null,
    state_at_12   binary(1)    null,
    state_at_13   binary(1)    null,
    state_at_14   binary(1)    null,
    state_at_15   binary(1)    null,
    state_at_16   binary(1)    null,
    state_at_17   binary(1)    null,
    state_at_18   binary(1)    null,
    state_at_19   binary(1)    null,
    state_at_20   binary(1)    null,
    state_at_21   binary(1)    null,
    state_at_22   binary(1)    null,
    state_at_23   binary(1)    null
);

INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (0, 'always off uk', 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30);
INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (1, 'always on uk', 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31);
INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (2, 'awake hours uk', 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31);

