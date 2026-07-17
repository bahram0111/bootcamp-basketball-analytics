import models
from crud import create_many
from db_connection import engine
from session import get_session
import pandas as pd

# players_df = pd.DataFrame()

# def main():
#
#
#     with get_session() as session:
#
#         create_many(session, Player, players_df.to_dict("records"))
#
#         create_many(session, Team, teams_df.to_dict("records"))
#
#         create_many(session, Season, seasons_df.to_dict("records"))
#
#         create_many(session, Game, games_df.to_dict("records"))
#
#         create_many(session, PlayerSeasonStats, players_season_stats_df.to_dict("records"))
#
#         create_many(session, TeamSeasonInfo, teams_season_info_df.to_dict("records"))
#
#         create_many(session, Award, awards_df.to_dict("records"))
#
#         create_many(session, TeamGameStats, teams_gate_stats_df.to_dict("records"))
#
#
#
#
# if __name__ == "__main__":
#     main()


models.Base.metadata.create_all(engine)