from database import Player, Team, Season, Game, Player_Game_Stats, Team_Game_Stats, Award
from sqlalchemy.orm import Session
from datetime import date


def create_player(session: Session,
                  player_name:str,
                  birth_date:date,
                  height:int,
                  weight:int,
                  position:str,
                  college:str,
                  draft_year:int,
                  win_shares:int,
                  per:int
                  ):
    player = Player(
        player_name=player_name,
        birth_date=birth_date,
        height=height,
        weight=weight,
        position=position,
        college=college,
        draft_year=draft_year,
        win_shares=win_shares,
        PER=per
    )
    session.add(player)
    # session.commit()
    # session.refresh(player)

    return player

def get_players(session):

    return session.query(Player).all()

def delete_player(session, player_id):

    player = session.get(Player, player_id)

    session.delete(player)
    session.commit()