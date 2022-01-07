create table cloudmanager.scenario_hour
(
    id_scenario     integer NOT NULL PRIMARY KEY,
    name_scenario varchar(255) null,
    state_at_0    BOOLEAN    null,
    state_at_1    BOOLEAN    null,
    state_at_2    BOOLEAN    null,
    state_at_3    BOOLEAN    null,
    state_at_4    BOOLEAN    null,
    state_at_5    BOOLEAN    null,
    state_at_6    BOOLEAN    null,
    state_at_7    BOOLEAN    null,
    state_at_8    BOOLEAN    null,
    state_at_9    BOOLEAN    null,
    state_at_10   BOOLEAN    null,
    state_at_11   BOOLEAN    null,
    state_at_12   BOOLEAN    null,
    state_at_13   BOOLEAN    null,
    state_at_14   BOOLEAN    null,
    state_at_15   BOOLEAN    null,
    state_at_16   BOOLEAN    null,
    state_at_17   BOOLEAN    null,
    state_at_18   BOOLEAN    null,
    state_at_19   BOOLEAN    null,
    state_at_20   BOOLEAN    null,
    state_at_21   BOOLEAN    null,
    state_at_22   BOOLEAN    null,
    state_at_23   BOOLEAN    null
);

INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (0, 'always off uk', FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE);
INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (1, 'always on uk', TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
INSERT INTO cloudmanager.scenario_hour (id_scenario, name_scenario, state_at_0, state_at_1, state_at_2, state_at_3, state_at_4, state_at_5, state_at_6, state_at_7, state_at_8, state_at_9, state_at_10, state_at_11, state_at_12, state_at_13, state_at_14, state_at_15, state_at_16, state_at_17, state_at_18, state_at_19, state_at_20, state_at_21, state_at_22, state_at_23) VALUES (2, 'awake hours uk', FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);

