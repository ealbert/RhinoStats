__author__ = 'eagleiser'


class AccountStatsFixtures(object):

    @classmethod
    def standard_accounts_record(cls):
        return {
            "status": "ok",
            "meta": {
                "count": 1
            },
            "data": {
                "512841364": {
                    "stronghold_skirmish": {
                        "spotted": 666,
                        "direct_hits_received": 3260,
                        "explosion_hits": 2,
                        "piercings_received": 2727,
                        "piercings": 2819,
                        "xp": 294027,
                        "survived_battles": 255,
                        "dropped_capture_points": 1631,
                        "hits_percents": 66,
                        "draws": 13,
                        "battles": 731,
                        "damage_received": 541358,
                        "frags": 502,
                        "capture_points": 1441,
                        "hits": 3405,
                        "battle_avg_xp": 402,
                        "wins": 294,
                        "losses": 424,
                        "damage_dealt": 522978,
                        "no_damage_direct_hits_received": 533,
                        "shots": 5124,
                        "explosion_hits_received": 23,
                        "tanking_factor": 0.22
                    },
                    "account_id": 512841364,
                    "week_resources_earned": 0,
                    "stronghold_defense": {
                        "spotted": 8,
                        "direct_hits_received": 50,
                        "explosion_hits": 0,
                        "piercings_received": 32,
                        "piercings": 18,
                        "xp": 1994,
                        "survived_battles": 4,
                        "dropped_capture_points": 0,
                        "hits_percents": 55,
                        "draws": 1,
                        "battles": 9,
                        "damage_received": 12045,
                        "frags": 3,
                        "capture_points": 0,
                        "hits": 47,
                        "battle_avg_xp": 222,
                        "wins": 3,
                        "losses": 5,
                        "damage_dealt": 7828,
                        "no_damage_direct_hits_received": 18,
                        "shots": 86,
                        "explosion_hits_received": 1,
                        "tanking_factor": 0.69
                    },
                    "clan_id": 500050913,
                    "total_resources_earned": 5002
                }
            }
        }

    @classmethod
    def personal_data_response(cls):
        return {
        "status": "ok",
        "meta": {
            "count": 1
        },
        "data": {
            "512841364": {
                "client_language": "es",
                "last_battle_time": 1443204940,
                "account_id": 512841364,
                "created_at": 1375773230,
                "updated_at": 1443283176,
                "private": None,
                "ban_time": None,
                "global_rating": 5733,
                "clan_id": 500050913,
                "statistics": {
                    "max_frags_tank_id": 33,
                    "clan": {
                        "spotted": 37,
                        "avg_damage_assisted_track": 131.35,
                        "avg_damage_blocked": 532.56,
                        "direct_hits_received": 210,
                        "explosion_hits": 0,
                        "piercings_received": 143,
                        "piercings": 195,
                        "xp": 25839,
                        "survived_battles": 22,
                        "dropped_capture_points": 107,
                        "hits_percents": 76,
                        "draws": 1,
                        "battles": 46,
                        "damage_received": 60736,
                        "avg_damage_assisted": 382.7,
                        "frags": 26,
                        "avg_damage_assisted_radio": 251.35,
                        "capture_points": 43,
                        "hits": 270,
                        "battle_avg_xp": 562,
                        "wins": 18,
                        "losses": 27,
                        "damage_dealt": 74237,
                        "no_damage_direct_hits_received": 67,
                        "shots": 353,
                        "explosion_hits_received": 15,
                        "tanking_factor": 0.41
                    },
                    "max_xp_tank_id": 51713,
                    "regular_team": {
                        "spotted": 2,
                        "avg_damage_assisted_track": 108.67,
                        "max_xp": 1888,
                        "avg_damage_blocked": 721.67,
                        "direct_hits_received": 14,
                        "explosion_hits": 0,
                        "piercings_received": 7,
                        "piercings": 18,
                        "max_damage_tank_id": 5377,
                        "xp": 3344,
                        "survived_battles": 2,
                        "dropped_capture_points": 0,
                        "hits_percents": 88,
                        "draws": 0,
                        "max_xp_tank_id": 5377,
                        "battles": 3,
                        "damage_received": 1921,
                        "avg_damage_assisted": 196.67,
                        "max_frags_tank_id": 5377,
                        "frags": 5,
                        "avg_damage_assisted_radio": 88,
                        "capture_points": 0,
                        "max_damage": 2991,
                        "hits": 21,
                        "battle_avg_xp": 1115,
                        "wins": 2,
                        "losses": 1,
                        "damage_dealt": 5644,
                        "no_damage_direct_hits_received": 7,
                        "max_frags": 2,
                        "shots": 24,
                        "explosion_hits_received": 0,
                        "tanking_factor": 1.08
                    },
                    "max_xp": 2113,
                    "company": {
                        "spotted": 39,
                        "avg_damage_assisted_track": 32.75,
                        "avg_damage_blocked": 288.42,
                        "direct_hits_received": 217,
                        "explosion_hits": 0,
                        "piercings_received": 184,
                        "piercings": 151,
                        "xp": 16734,
                        "survived_battles": 10,
                        "dropped_capture_points": 128,
                        "hits_percents": 67,
                        "draws": 0,
                        "battles": 57,
                        "damage_received": 49800,
                        "avg_damage_assisted": 192.96,
                        "frags": 22,
                        "avg_damage_assisted_radio": 160.21,
                        "capture_points": 0,
                        "hits": 212,
                        "battle_avg_xp": 294,
                        "wins": 13,
                        "losses": 44,
                        "damage_dealt": 40679,
                        "no_damage_direct_hits_received": 33,
                        "shots": 318,
                        "explosion_hits_received": 8,
                        "tanking_factor": 0.36
                    },
                    "trees_cut": 41834,
                    "all": {
                        "spotted": 19466,
                        "avg_damage_assisted_track": 62.29,
                        "max_xp": 2113,
                        "avg_damage_blocked": 316.01,
                        "direct_hits_received": 99183,
                        "explosion_hits": 1991,
                        "piercings_received": 74717,
                        "piercings": 89091,
                        "max_damage_tank_id": 8193,
                        "xp": 14471022,
                        "survived_battles": 8915,
                        "dropped_capture_points": 20140,
                        "hits_percents": 64,
                        "draws": 242,
                        "max_xp_tank_id": 51713,
                        "battles": 25346,
                        "damage_received": 21158971,
                        "avg_damage_assisted": 322.94,
                        "max_frags_tank_id": 33,
                        "frags": 18350,
                        "avg_damage_assisted_radio": 260.65,
                        "capture_points": 21351,
                        "max_damage": 6520,
                        "hits": 131364,
                        "battle_avg_xp": 571,
                        "wins": 12270,
                        "losses": 12834,
                        "damage_dealt": 22084121,
                        "no_damage_direct_hits_received": 24466,
                        "max_frags": 8,
                        "shots": 205245,
                        "explosion_hits_received": 3111,
                        "tanking_factor": 0.33
                    },
                    "globalmap_absolute": {
                        "spotted": 26,
                        "avg_damage_assisted_track": 154.92,
                        "avg_damage_blocked": 546.41,
                        "direct_hits_received": 190,
                        "explosion_hits": 0,
                        "piercings_received": 125,
                        "piercings": 174,
                        "xp": 21219,
                        "survived_battles": 19,
                        "dropped_capture_points": 107,
                        "hits_percents": 76,
                        "draws": 1,
                        "battles": 39,
                        "damage_received": 54538,
                        "avg_damage_assisted": 402.13,
                        "frags": 25,
                        "avg_damage_assisted_radio": 247.21,
                        "capture_points": 38,
                        "hits": 246,
                        "battle_avg_xp": 544,
                        "wins": 13,
                        "losses": 25,
                        "damage_dealt": 66197,
                        "no_damage_direct_hits_received": 65,
                        "shots": 322,
                        "explosion_hits_received": 15,
                        "tanking_factor": 0.41
                    },
                    "globalmap_middle": {
                        "spotted": 0,
                        "avg_damage_assisted_track": 0,
                        "avg_damage_blocked": 135,
                        "direct_hits_received": 3,
                        "explosion_hits": 0,
                        "piercings_received": 2,
                        "piercings": 1,
                        "xp": 21,
                        "survived_battles": 0,
                        "dropped_capture_points": 0,
                        "hits_percents": 50,
                        "draws": 0,
                        "battles": 1,
                        "damage_received": 750,
                        "avg_damage_assisted": 0,
                        "frags": 0,
                        "avg_damage_assisted_radio": 0,
                        "capture_points": 0,
                        "hits": 1,
                        "battle_avg_xp": 21,
                        "wins": 0,
                        "losses": 1,
                        "damage_dealt": 130,
                        "no_damage_direct_hits_received": 1,
                        "shots": 2,
                        "explosion_hits_received": 0,
                        "tanking_factor": 0.5
                    },
                    "stronghold_defense": {
                        "spotted": 8,
                        "max_frags_tank_id": 17153,
                        "max_xp": 867,
                        "direct_hits_received": 50,
                        "explosion_hits": 0,
                        "piercings_received": 32,
                        "piercings": 18,
                        "xp": 1994,
                        "survived_battles": 4,
                        "dropped_capture_points": 0,
                        "hits_percents": 55,
                        "draws": 0,
                        "max_xp_tank_id": 7169,
                        "battles": 9,
                        "damage_received": 12045,
                        "frags": 3,
                        "capture_points": 0,
                        "max_damage_tank_id": 7169,
                        "max_damage": 3599,
                        "hits": 47,
                        "battle_avg_xp": 222,
                        "wins": 3,
                        "losses": 6,
                        "damage_dealt": 7828,
                        "no_damage_direct_hits_received": 18,
                        "max_frags": 1,
                        "shots": 86,
                        "explosion_hits_received": 1,
                        "tanking_factor": 0.69
                    },
                    "stronghold_skirmish": {
                        "spotted": 679,
                        "max_frags_tank_id": 1105,
                        "max_xp": 1813,
                        "direct_hits_received": 3337,
                        "explosion_hits": 2,
                        "piercings_received": 2787,
                        "piercings": 2881,
                        "xp": 301881,
                        "survived_battles": 267,
                        "dropped_capture_points": 1631,
                        "hits_percents": 66,
                        "draws": 14,
                        "max_xp_tank_id": 1105,
                        "battles": 755,
                        "damage_received": 554958,
                        "frags": 516,
                        "capture_points": 1472,
                        "max_damage_tank_id": 5377,
                        "max_damage": 2981,
                        "hits": 3476,
                        "battle_avg_xp": 400,
                        "wins": 307,
                        "losses": 434,
                        "damage_dealt": 541543,
                        "no_damage_direct_hits_received": 550,
                        "max_frags": 5,
                        "shots": 5228,
                        "explosion_hits_received": 23,
                        "tanking_factor": 0.22
                    },
                    "historical": {
                        "spotted": 0,
                        "avg_damage_assisted_track": 0,
                        "max_xp": 0,
                        "avg_damage_blocked": 0,
                        "direct_hits_received": 0,
                        "explosion_hits": 0,
                        "piercings_received": 0,
                        "piercings": 0,
                        "max_damage_tank_id": None,
                        "xp": 0,
                        "survived_battles": 0,
                        "dropped_capture_points": 0,
                        "hits_percents": 0,
                        "draws": 0,
                        "max_xp_tank_id": None,
                        "battles": 0,
                        "damage_received": 0,
                        "avg_damage_assisted": 0,
                        "max_frags_tank_id": None,
                        "frags": 0,
                        "avg_damage_assisted_radio": 0,
                        "capture_points": 0,
                        "max_damage": 0,
                        "hits": 0,
                        "battle_avg_xp": 0,
                        "wins": 0,
                        "losses": 0,
                        "damage_dealt": 0,
                        "no_damage_direct_hits_received": 0,
                        "max_frags": 0,
                        "shots": 0,
                        "explosion_hits_received": 0,
                        "tanking_factor": 0
                    },
                    "team": {
                        "spotted": 588,
                        "avg_damage_assisted_track": 49.79,
                        "max_xp": 2218,
                        "avg_damage_blocked": 278.74,
                        "direct_hits_received": 2915,
                        "explosion_hits": 1,
                        "piercings_received": 2150,
                        "piercings": 2630,
                        "max_damage_tank_id": 2849,
                        "xp": 414725,
                        "survived_battles": 299,
                        "dropped_capture_points": 1119,
                        "hits_percents": 70,
                        "draws": 38,
                        "max_xp_tank_id": 2849,
                        "battles": 689,
                        "damage_received": 514338,
                        "avg_damage_assisted": 152.31,
                        "max_frags_tank_id": 5377,
                        "frags": 422,
                        "avg_damage_assisted_radio": 102.52,
                        "capture_points": 1659,
                        "max_damage": 4145,
                        "hits": 3758,
                        "battle_avg_xp": 602,
                        "wins": 362,
                        "losses": 289,
                        "damage_dealt": 613827,
                        "no_damage_direct_hits_received": 765,
                        "max_frags": 4,
                        "shots": 5372,
                        "explosion_hits_received": 2,
                        "tanking_factor": 0.33
                    },
                    "max_damage_tank_id": 8193,
                    "frags": None,
                    "max_damage": 6520,
                    "max_damage_vehicle": 8193,
                    "globalmap_champion": {
                        "spotted": 11,
                        "avg_damage_assisted_track": 0,
                        "avg_damage_blocked": 65,
                        "direct_hits_received": 17,
                        "explosion_hits": 0,
                        "piercings_received": 16,
                        "piercings": 20,
                        "xp": 4599,
                        "survived_battles": 3,
                        "dropped_capture_points": 0,
                        "hits_percents": 79,
                        "draws": 0,
                        "battles": 6,
                        "damage_received": 5448,
                        "avg_damage_assisted": 320.17,
                        "frags": 1,
                        "avg_damage_assisted_radio": 320.17,
                        "capture_points": 5,
                        "hits": 23,
                        "battle_avg_xp": 767,
                        "wins": 5,
                        "losses": 1,
                        "damage_dealt": 7910,
                        "no_damage_direct_hits_received": 1,
                        "shots": 29,
                        "explosion_hits_received": 0,
                        "tanking_factor": 0.25
                    },
                    "max_frags": 8
                },
                "nickname": "test-player",
                "ban_info": None,
                "logout_at": 1443283173
            }
        }
    }
