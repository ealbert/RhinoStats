DROP TABLE IF EXISTS player_stats;
CREATE TABLE player_stats(
  clan_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  account_name TEXT NOT NULL,
  total_resources_earned INTEGER NOT NULL,
  seven_day_resources_earned INTEGER NOT NULL,
  thirty_day_resources_earned INTEGER NOT NULL,
  stronghold_defense_battles INTEGER NOT NULL,
  thirty_day_defense_battles INTEGER NOT NULL,
  stronghold_skirmish_battles INTEGER NOT NULL,
  thirty_day_skirmish_battles INTEGER NOT NULL,
  created_date timestamp NOT NULL,
  last_update timestamp NOT NULL
);

DROP TABLE IF EXISTS player_stats_snapshot;
CREATE TABLE player_stats_snapshot(
  clan_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  total_resources_earned INTEGER NOT NULL,
  stronghold_defense_battles INTEGER NOT NULL,
  stronghold_skirmish_battles INTEGER NOT NULL,
  created_date timestamp NOT NULL
);