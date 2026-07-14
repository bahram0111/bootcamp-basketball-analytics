from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
#--------------------------------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = 'players'
    player_id : Mapped[str] = mapped_column( primary_key=True , autoincrement=True)  #data type has changed from int to str
    player_name : Mapped[str]
    birth_date : Mapped[date]
    height : Mapped[int]
    weight : Mapped[int]
    position : Mapped[str]
    college : Mapped[str]
    draft_year : Mapped[int]
    win_shares : Mapped[int]            #these are some well-known KPIs I have added
    PER : Mapped[int]   
    awards : Mapped[list["Award"]] = relationship(back_populates="player")
    player_game_stats : Mapped[list["Player_Game_Stats"]] = relationship(back_populates="player")    
    
    
#--------------------------------------------------------------------------------------------------

class Team(Base):
    __tablename__ = 'teams'
    team_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    team_name : Mapped[str]
    city : Mapped[str]
    conference : Mapped[int]        #not sure about its type
    division : Mapped[int]   #not sure about its type
    team_game_stats:Mapped[list["Team_Game_Stats"]] = relationship(back_populates="team") 
    player_game_stats : Mapped[list["Player_Game_Stats"]] = relationship(back_populates="team")
#--------------------------------------------------------------------------------------------------

class Season(Base):
    __tablename__ = 'seasons'
    season_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    start_year : Mapped[int]
    end_year : Mapped[int]
    games:Mapped[list["Game"]]=relationship(back_populates="season")
    awards:Mapped[list["Award"]]=relationship(back_populates="season")
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
    player_game_stats:Mapped[list["Player_Game_Stats"]]=relationship(back_populates="game")
    team_game_stats : Mapped[list["Team_Game_Stats"]] = relationship(back_populates="game")
    season:Mapped["Season"]=relationship(back_populates="games")
#--------------------------------------------------------------------------------------------------

class Player_Game_Stats(Base):
    __tablename__ = 'player_game_stats'
    id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    player_id : Mapped[str] = mapped_column(db.ForeignKey('players.player_id'))  #data type has changed from int to str
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
    player : Mapped["Player"] = relationship(back_populates="player_game_stats")    
    games: Mapped["Game"] = relationship(back_populates="player_game_stats") 
    team : Mapped["Team"] = relationship(back_populates="player_game_stats")
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
    team:Mapped["Team"] = relationship(back_populates="team_game_stats") 
    game:Mapped["Game"] = relationship(back_populates="team_game_stats")
#--------------------------------------------------------------------------------------------------

class Award(Base):
    __tablename__ = 'awards'
    award_id : Mapped[int] = mapped_column( primary_key=True , autoincrement=True)
    player_id : Mapped[int] = mapped_column(db.ForeignKey('players.player_id'))
    season_id : Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    award_name : Mapped[str]
    player:Mapped["Player"] = relationship(back_populates="awards")
    season:Mapped["Season"] = relationship(back_populates="awards")
    