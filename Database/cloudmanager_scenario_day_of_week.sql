create table cloudmanager.scenario_day_of_week
(
    id_scenario     integer NOT NULL PRIMARY KEY,
    name_scenario   varchar(255) null,
    state_Monday    BOOLEAN    null,
    state_Tuesday   BOOLEAN    null,
    state_Wednesday BOOLEAN    null,
    state_Thursday  BOOLEAN    null,
    state_Friday    BOOLEAN    null,
    state_Saturday  BOOLEAN    null,
    state_Sunday    BOOLEAN    null
);

INSERT INTO cloudmanager.scenario_day_of_week (id_scenario, name_scenario, state_Monday, state_Tuesday, state_Wednesday, state_Thursday, state_Friday, state_Saturday, state_Sunday) VALUES (0, 'always off', FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE);
