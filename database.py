from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint
from datetime import date

# --------------------------------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

# --------------------------------------------------------------------------------------------------


class Player(Base):
    __tablename__ = 'players'
    player_id: Mapped[int] = mapped_column(primary_key=True)  
    player_name: Mapped[str]
    birth_date: Mapped[date]
    height: Mapped[int]      
    weight: Mapped[int]       
    position: Mapped[str]
    college: Mapped[str] = mapped_column(nullable=True)  # ADDED: nullable - many players skip college
    draft_year: Mapped[int] = mapped_column(nullable=True)  # ADDED: nullable - undrafted players exist

    season_stats: Mapped[list["Player_Season_Stats"]] = relationship(back_populates="player")
    awards: Mapped[list["Award"]] = relationship(back_populates="player")


# --------------------------------------------------------------------------------------------------

class Team(Base):
    __tablename__ = 'teams'
    team_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_name: Mapped[str]
    city: Mapped[str]
    conference: Mapped[str]   # "Eastern" / "Western"
    division: Mapped[str]     # "Atlantic", "Pacific", ...
    founding_year: Mapped[int]  # ADDED: team founding year
    league: Mapped[str]       # ADDED: e.g. "NBA"

    season_stats: Mapped[list["Player_Season_Stats"]] = relationship(back_populates="team")
    games_as_home: Mapped[list["Game"]] = relationship(back_populates="home_team", foreign_keys="Game.home_team_id")
    games_as_away: Mapped[list["Game"]] = relationship(back_populates="away_team", foreign_keys="Game.away_team_id")
    team_game_stats: Mapped[list["Team_Game_Stats"]] = relationship(back_populates="team")
    season_info: Mapped[list["Team_Season_Info"]] = relationship(back_populates="team")  # ADDED


# --------------------------------------------------------------------------------------------------

class Season(Base):
    __tablename__ = 'seasons'
    season_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_year: Mapped[int]
    end_year: Mapped[int]
    champion_team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'), nullable=True)  # ADDED: links to the team that won this season's championship
    champion_team: Mapped["Team"] = relationship()
    player_stats: Mapped[list["Player_Season_Stats"]] = relationship(back_populates="season")
    awards: Mapped[list["Award"]] = relationship(back_populates="season")
    games: Mapped[list["Game"]] = relationship(back_populates="season")
    team_info: Mapped[list["Team_Season_Info"]] = relationship(back_populates="season")  # ADDED


# --------------------------------------------------------------------------------------------------

class Player_Season_Stats(Base):
    __tablename__ = 'player_season_stats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(db.ForeignKey('players.player_id'))
    season_id: Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))            
    experience: Mapped[int]        
    is_active: Mapped[bool]
    games_played: Mapped[int]
    minutes_per_game: Mapped[float]
    points_per_game: Mapped[float]
    rebounds_per_game: Mapped[float]
    assists_per_game: Mapped[float]
    steals_per_game: Mapped[float]
    blocks_per_game: Mapped[float]
    turnovers_per_game: Mapped[float]
    field_goal_percentage: Mapped[float]
    three_point_percentage: Mapped[float]
    free_throw_percentage: Mapped[float]
    salary:Mapped[int]
    player: Mapped["Player"] = relationship(back_populates="season_stats")
    season: Mapped["Season"] = relationship(back_populates="player_stats")
    team: Mapped["Team"] = relationship(back_populates="season_stats")

    __table_args__ = (
        UniqueConstraint('player_id', 'season_id', 'team_id', name='uq_player_season_team'),
    )



# --------------------------------------------------------------------------------------------------

# ADDED: entire new table - per-team, per-season record (wins, losses, coach, star player, roster averages)
# --------------------------------------------------------------------------------------------------

class Team_Season_Info(Base):  # ADDED: new table
    __tablename__ = 'team_season_info'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # ADDED
    team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))  # ADDED
    season_id: Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))  # ADDED
    wins: Mapped[int]  # ADDED
    losses: Mapped[int]  # ADDED
    coach_name: Mapped[str]  # ADDED
    star_player_id: Mapped[int] = mapped_column(db.ForeignKey('players.player_id'), nullable=True)  # ADDED: nullable
    avg_height: Mapped[float]  # ADDED: roster average height for the season
    avg_weight: Mapped[float]  # ADDED: roster average weight for the season
    avg_age: Mapped[float]     # ADDED: roster average age for the season

    team: Mapped["Team"] = relationship(back_populates="season_info")  # ADDED
    season: Mapped["Season"] = relationship(back_populates="team_info")  # ADDED
    star_player: Mapped["Player"] = relationship()  # ADDED: one-way, no back_populates 

    __table_args__ = (
        UniqueConstraint('team_id', 'season_id', name='uq_team_season'),  # ADDED
    )


# --------------------------------------------------------------------------------------------------

class Award(Base):
    __tablename__ = 'awards'
    award_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(db.ForeignKey('players.player_id'))
    season_id: Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    award_name: Mapped[str]   

    player: Mapped["Player"] = relationship(back_populates="awards")
    season: Mapped["Season"] = relationship(back_populates="awards")


# --------------------------------------------------------------------------------------------------

class Game(Base):
    __tablename__ = 'games'
    game_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    season_id: Mapped[int] = mapped_column(db.ForeignKey('seasons.season_id'))
    date: Mapped[date]
    home_team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))
    away_team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))
    home_score: Mapped[int]
    away_score: Mapped[int]
    playoff: Mapped[bool]
    season: Mapped["Season"] = relationship(back_populates="games")
    home_team: Mapped["Team"] = relationship(back_populates="games_as_home", foreign_keys=[home_team_id])
    away_team: Mapped["Team"] = relationship(back_populates="games_as_away", foreign_keys=[away_team_id])
    team_game_stats: Mapped[list["Team_Game_Stats"]] = relationship(back_populates="game")


class Team_Game_Stats(Base):
    __tablename__ = 'team_game_stats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(db.ForeignKey('teams.team_id'))
    game_id: Mapped[int] = mapped_column(db.ForeignKey('games.game_id'))
    points: Mapped[int]
    field_goal_percentage: Mapped[float]
    three_point_percentage: Mapped[float]
    rebounds: Mapped[int]
    assists: Mapped[int]
    turnovers: Mapped[int]

    team: Mapped["Team"] = relationship(back_populates="team_game_stats")
    game: Mapped["Game"] = relationship(back_populates="team_game_stats")