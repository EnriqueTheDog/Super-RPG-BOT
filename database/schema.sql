CREATE TABLE IF NOT EXISTS `blacklist` (
  `user_id` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `warns` (
  `id` int(11) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `server_id` varchar(20) NOT NULL,
  `moderator_id` varchar(20) NOT NULL,
  `reason` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `persona` (
    `id` int(11) NOT NULL,
    `owner_id` varchar(20) NOT NULL,
    `server_id` varchar(20) NOT NULL,
    `last_check` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `name` varchar(50) NOT NULL,
    `race` varchar(100) NOT NULL,
    `class` varchar(100) NOT NULL,
    `gender` smallint NOT NULL,
    `kills` int NOT NULL,
    `hp` int NOT NULL,
    `stamina` int NOT NULL,
    `mana` int NOT NULL,
    `strength` int NOT NULL,
    `dexterity` int NOT NULL,
    `knowledge` int NOT NULL,
    `faith` int NOT NULL,
    `health` int NOT NULL,
    `vitality` int NOT NULL,
    `endurance` int NOT NULL,
    `cardio` int NOT NULL,
    `intelligence` int NOT NULL,
    `focus` int NOT NULL,
    `left_handed` bit NOT NULL,
    `ambidextrous` bit NOT NULL
);

CREATE TABLE IF NOT EXISTS `item` (
    `id` int(11) NOT NULL,
    `server_id` varchar(20) NOT NULL,
    `name` varchar(100) NOT NULL,
    `lvl` int NOT NULL,
    `type` smallint NOT NULL,
    `base_power` int NOT NULL,
    `variability` int NOT NULL,
    `strength_bonus` int NOT NULL,
    `dexterity_bonus` int NOT NULL,
    `knowledge_bonus` int NOT NULL,
    `faith_bonus` int NOT NULL,
    `health_bonus` int NOT NULL,
    `vitality_bonus` int NOT NULL,
    `endurance_bonus` int NOT NULL,
    `cardio_bonus` int NOT NULL,
    `intelligence_bonus` int NOT NULL,
    `focus_bonus` int NOT NULL
);

CREATE TABLE IF NOT EXISTS `persona_item` (
    `id` int(11) NOT NULL,
    `persona_id` int(11) NOT NULL,
    `item_id` int(11) NOT NULL,
    `equipped_left` bit NOT NULL,
    `equipped_right` bit NOT NULL
);

