from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
#--------------------------------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = 'players'
    player_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    player_name : Mapped[str]
    birth_date : Mapped[date]
    height : Mapped[int]
    weight : Mapped[int]
    position : Mapped[str]
    college : Mapped[str]
    draft_year : Mapped[int]
    win_shares : Mapped[int]            #these are some well-known KPIs I have added
    PER : Mapped[int]
#--------------------------------------------------------------------------------------------------

class Team(Base):
    __tablename__ = 'teams'
    team_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    team_name : Mapped[str]
    city : Mapped[str]
    conference : Mapped[int]        #not sure about its type
    division : Mapped[int]          #not sure about its type

#--------------------------------------------------------------------------------------------------

class Season(Base):
    __tablename__ = 'seasons'
    season_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    start_year : Mapped[int]
    end_year : Mapped[int]

#--------------------------------------------------------------------------------------------------

class Game(Base):
    __tablename__ = 'games'
    game_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    season_id : Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    date : Mapped[date]
    home_team : Mapped[str]
    away_team : Mapped[str]
    home_score : Mapped[int]
    away_score : Mapped[int]
    playoff : Mapped[int]

#--------------------------------------------------------------------------------------------------

class Player_Game_Stats(Base):
    __tablename__ = 'player_game_stats'
    id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    player_id : Mapped[int] = mapped_column(db.ForeignKey('players.player_id'))
    game_id : Mapped[int] = mapped_column(db.ForeignKey('games.game_id'))
    team_id : Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))
    minutes : Mapped[int]
    points : Mapped[int]
    rebounds : Mapped[int]
    assists : Mapped[int]
    steals : Mapped[int]
    blocks : Mapped[int]
    turnovers : Mapped[int]
    field_goals : Mapped[int]
    field_goal_attempts : Mapped[int]
    three_P : Mapped[int]
    three_PA : Mapped[int]
    free_throws : Mapped[int]
    free_throw_attempts : Mapped[int]
    points_per_game : Mapped[int]            #added this one,was not part of the document
    plus_minus : Mapped[int]

#--------------------------------------------------------------------------------------------------

class Team_Game_Stats(Base):
    __tablename__ = 'team_game_stats'
    id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    team_id : Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))
    game_id : Mapped[int] = mapped_column(db.ForeignKey('games.game_id'))
    points : Mapped[int]
    field_goal_percentage : Mapped[int]
    FTA : Mapped[int]
    three_PP : Mapped[int]
    rebounds : Mapped[int]
    assists : Mapped[int]
    turnovers : Mapped[int]

#--------------------------------------------------------------------------------------------------

class Award(Base):
    __tablename__ = 'awards'
    award_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    player_id : Mapped[int] = mapped_column(db.ForeignKey('players.player_id'))
    season_id : Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    award_name : Mapped[str]