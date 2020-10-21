create table scenario_day_of_week
(
    id_scenario     int          not null
        primary key,
    name_scenario   varchar(255) null,
    state_Monday    binary(1)    null,
    state_Tuesday   binary(1)    null,
    state_Wednesday binary(1)    null,
    state_Thursday  binary(1)    null,
    state_Friday    binary(1)    null,
    state_Saturday  binary(1)    null,
    state_Sunday    binary(1)    null
);

INSERT INTO cloudmanager.scenario_day_of_week (id_scenario, name_scenario, state_Monday, state_Tuesday, state_Wednesday, state_Thursday, state_Friday, state_Saturday, state_Sunday) VALUES (0, 'always off', 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30);