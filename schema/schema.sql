ALTER TABLE player_stats ADD COLUMN clan_battles INTEGER NOT NULL DEFAULT 0;
ALTER TABLE player_stats ADD COLUMN thirty_day_clan_battles INTEGER NOT NULL DEFAULT 0;
ALTER TABLE player_stats ADD COLUMN all_battles INTEGER NOT NULL DEFAULT 0;
ALTER TABLE player_stats ADD COLUMN thirty_day_all_battles INTEGER NOT NULL DEFAULT 0;

ALTER TABLE player_stats_snapshot ADD COLUMN clan_battles INTEGER NOT NULL DEFAULT 0;
ALTER TABLE player_stats_snapshot ADD COLUMN all_battles INTEGER NOT NULL DEFAULT 0;
