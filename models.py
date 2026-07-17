from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UniqueConstraint
from datetime import date

# --------------------------------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

# --------------------------------------------------------------------------------------------------


class Player(Base):
    __tablename__ = 'players'
    player_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date)
    height_cm: Mapped[int] = mapped_column(Integer)
    weight_kg: Mapped[int] = mapped_column(Integer)
    position: Mapped[str] = mapped_column(String(20))
    college: Mapped[str] = mapped_column(String(100))
    draft_year: Mapped[int] = mapped_column(Integer)
    nba_debut: Mapped[int] = mapped_column(Integer)
    experience_years: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[int] = mapped_column(Integer)
    birth_place: Mapped[str] = mapped_column(String(100))
    shoots: Mapped[str] = mapped_column(String(10))




# --------------------------------------------------------------------------------------------------

class Team(Base):
    __tablename__ = 'teams'
    team_id: Mapped[int] = mapped_column(Integer ,primary_key=True)
    team_name: Mapped[str] = mapped_column(String(100), nullable=False)
    from_year: Mapped[int] = mapped_column(Integer)
    to_year: Mapped[int] = mapped_column(Integer)
    years: Mapped[int] = mapped_column(Integer)
    total_games: Mapped[int] = mapped_column(Integer)
    total_wins: Mapped[int] = mapped_column(Integer)
    total_losses: Mapped[int] = mapped_column(Integer)
    win_percentage: Mapped[float] = mapped_column(Numeric(5,2))
    playoffs: Mapped[int] = mapped_column(Integer)
    conference_championships: Mapped[int] = mapped_column(Integer)
    division_championships: Mapped[int] = mapped_column(Integer)
    championships: Mapped[int] = mapped_column(Integer)
    league: Mapped[str] = mapped_column(String(10))



# --------------------------------------------------------------------------------------------------

class Season(Base):
    __tablename__ = 'seasons'
    season_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    season: Mapped[str] = mapped_column(String(10))


# --------------------------------------------------------------------------------------------------

class PlayerSeasonStats(Base):
    __tablename__ = 'player_season_stats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.player_id"))
    season_id: Mapped[int] = mapped_column(ForeignKey('seasons.season_id'))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    rank: Mapped[int] = mapped_column(Integer)
    age: Mapped[int] = mapped_column(Integer)
    position: Mapped[str] = mapped_column(String(20))
    games: Mapped[int] = mapped_column(Integer)
    games_started: Mapped[int] = mapped_column(Integer)
    minutes_played:Mapped[int] = mapped_column(Integer)
    field_goals: Mapped[int] = mapped_column(Integer)
    field_goals_attempted: Mapped[int] = mapped_column(Integer)
    field_goals_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    three_point_field_goals: Mapped[int] = mapped_column(Integer)
    three_point_field_goal_attempted: Mapped[int] = mapped_column(Integer)
    three_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    two_point_field_goals: Mapped[int] = mapped_column(Integer)
    two_point_field_goal_attempted: Mapped[int] = mapped_column(Integer)
    two_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    effective_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    free_throws: Mapped[int] = mapped_column(Integer)
    free_throws_attempted: Mapped[int] = mapped_column(Integer)
    free_throws_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    offensive_rebounds: Mapped[int] = mapped_column(Integer)
    defensive_rebounds: Mapped[int] = mapped_column(Integer)
    total_rebounds: Mapped[int] = mapped_column(Integer)
    assists: Mapped[int] = mapped_column(Integer)
    steals: Mapped[int] = mapped_column(Integer)
    blocks: Mapped[int] = mapped_column(Integer)
    turnovers: Mapped[int] = mapped_column(Integer)
    points: Mapped[int] = mapped_column(Integer)
    personal_fouls: Mapped[int] = mapped_column(Integer)
    triple_doubles: Mapped[int] = mapped_column(Integer)



# --------------------------------------------------------------------------------------------------

class TeamSeasonStats(Base):
    __tablename__ = 'team_season_stats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    season_id: Mapped[int] = mapped_column(ForeignKey('seasons.season_id'))
    league: Mapped[str] = mapped_column(String(10))
    wins: Mapped[int] = mapped_column(Integer)
    losses: Mapped[int] = mapped_column(Integer)
    win_loss_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    finish: Mapped[int] = mapped_column(Integer)
    average_height: Mapped[float] = mapped_column(Numeric(5,1))
    average_weight: Mapped[float] = mapped_column(Numeric(5,1))
    average_age: Mapped[float] = mapped_column(Numeric(4,1))
    simple_rating_system: Mapped[float] = mapped_column(Numeric(5,2))
    pace: Mapped[float] = mapped_column(Numeric(5,1))
    relative_pace: Mapped[float] = mapped_column(Numeric(5,1))
    offensive_rating: Mapped[float] = mapped_column(Numeric(5,1))
    relative_offensive_rating: Mapped[float] = mapped_column(Numeric(5,1))
    top_win_shares_player: Mapped[str] = mapped_column(String(100))
    games: Mapped[int] = mapped_column(Integer)
    minutes_played: Mapped[int] = mapped_column(Integer)
    field_goals: Mapped[int] = mapped_column(Integer)
    field_goals_attempted: Mapped[int] = mapped_column(Integer)
    field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    three_point_field_goals: Mapped[int] = mapped_column(Integer)
    three_point_field_goal_attempted: Mapped[int] = mapped_column(Integer)
    three_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    two_point_field_goals: Mapped[int] = mapped_column(Integer)
    two_point_field_goal_attempted: Mapped[int] = mapped_column(Integer)
    two_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    effective_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    free_throws: Mapped[int] = mapped_column(Integer)
    free_throws_attempted: Mapped[int] = mapped_column(Integer)
    free_throws_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    offensive_rebounds: Mapped[int] = mapped_column(Integer)
    defensive_rebounds: Mapped[int] = mapped_column(Integer)
    total_rebounds: Mapped[int] = mapped_column(Integer)
    assists: Mapped[int] = mapped_column(Integer)
    steals: Mapped[int] = mapped_column(Integer)
    blocks: Mapped[int] = mapped_column(Integer)
    turnovers: Mapped[int] = mapped_column(Integer)
    points: Mapped[int] = mapped_column(Integer)
    personal_fouls: Mapped[int] = mapped_column(Integer)



# --------------------------------------------------------------------------------------------------

class MvpVotes(Base):
    __tablename__ = 'MVP_votes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'))
    season_id: Mapped[int] = mapped_column(ForeignKey('seasons.season_id'))
    rank: Mapped[int] = mapped_column(Integer)
    first_place_votes: Mapped[int] = mapped_column(Integer)
    points_won: Mapped[int] = mapped_column(Integer)
    points_max: Mapped[int] = mapped_column(Integer)
    share: Mapped[float] = mapped_column(Numeric(5,3))
    win_shares: Mapped[float] = mapped_column(Numeric(5,1))
    win_shares_per_48: Mapped[float] = mapped_column(Numeric(5,3))
    games: Mapped[int] = mapped_column(Integer)
    minutes_played_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    points_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    total_rebounds_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    assists_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    steals_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    blocks_per_game: Mapped[float] = mapped_column(Numeric(5,1))
    field_goal_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    three_point_field_goal_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    free_throw_percentage: Mapped[float] = mapped_column(Numeric(5,3))

# --------------------------------------------------------------------------------------------------

class Champ(Base):
    __tablename__ = "champ"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.season_id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))