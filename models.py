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
    player_id: Mapped[int] = mapped_column(primary_key=True)
    player_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column()
    height_cm: Mapped[int] = mapped_column()
    weight_kg: Mapped[int] = mapped_column()
    position: Mapped[str] = mapped_column(String(20))
    college: Mapped[str] = mapped_column(String(100) , nullable=True)
    draft_year: Mapped[int] = mapped_column(nullable=True)
    nba_debut: Mapped[int] = mapped_column()
    experience_years: Mapped[int] = mapped_column() # I think the naming is weird
    is_active: Mapped[bool] = mapped_column()
    birth_place: Mapped[str] = mapped_column(String(100))
    shoots: Mapped[str] = mapped_column(String(10))




# --------------------------------------------------------------------------------------------------

class Team(Base):
    __tablename__ = 'teams'
    team_id: Mapped[int] = mapped_column(primary_key=True)
    team_name: Mapped[str] = mapped_column(String(100), nullable=False)
    from_year: Mapped[int] = mapped_column()
    to_year: Mapped[int] = mapped_column()
#    years: Mapped[int] = mapped_column()
#    total_games: Mapped[int] = mapped_column()
    total_wins: Mapped[int] = mapped_column()
    total_losses: Mapped[int] = mapped_column()
#    win_percentage: Mapped[float] = mapped_column(Numeric(5,2))
    playoffs: Mapped[int] = mapped_column()
    conference_championships: Mapped[int] = mapped_column()
    division_championships: Mapped[int] = mapped_column()
    championships: Mapped[int] = mapped_column()
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
    rank: Mapped[int] = mapped_column()
#    age: Mapped[int] = mapped_column()
    position: Mapped[str] = mapped_column(String(20))
    games: Mapped[int] = mapped_column()
    games_started: Mapped[int] = mapped_column()
    minutes_played:Mapped[int] = mapped_column()
    field_goals: Mapped[int] = mapped_column()
    field_goals_attempt: Mapped[int] = mapped_column()
#    field_goals_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    three_point_field_goals: Mapped[int] = mapped_column()
    three_point_field_goal_attempt: Mapped[int] = mapped_column()
#    three_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    two_point_field_goals: Mapped[int] = mapped_column()
    two_point_field_goal_attempt: Mapped[int] = mapped_column()
#    two_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    effective_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    free_throws: Mapped[int] = mapped_column()
    free_throws_attempt: Mapped[int] = mapped_column()
#    free_throws_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    offensive_rebounds: Mapped[int] = mapped_column()
    defensive_rebounds: Mapped[int] = mapped_column()
#    total_rebounds: Mapped[int] = mapped_column()
    assists: Mapped[int] = mapped_column()
    steals: Mapped[int] = mapped_column()
    blocks: Mapped[int] = mapped_column()
    turnovers: Mapped[int] = mapped_column()
    points: Mapped[int] = mapped_column()
    personal_fouls: Mapped[int] = mapped_column()
    triple_doubles: Mapped[int] = mapped_column()



# --------------------------------------------------------------------------------------------------

class TeamSeasonStats(Base):
    __tablename__ = 'team_season_stats'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    season_id: Mapped[int] = mapped_column(ForeignKey('seasons.season_id'))
    league: Mapped[str] = mapped_column(String(10))
    wins: Mapped[int] = mapped_column()
    losses: Mapped[int] = mapped_column()
#    win_loss_percentage: Mapped[float] = mapped_column(Numeric(5,3))
    finish: Mapped[int] = mapped_column()
    average_height: Mapped[float] = mapped_column(Numeric(5,1))
    average_weight: Mapped[float] = mapped_column(Numeric(5,1))
    average_age: Mapped[float] = mapped_column(Numeric(4,1))
    simple_rating_system: Mapped[float] = mapped_column(Numeric(5,2))
    pace: Mapped[float] = mapped_column(Numeric(5,1))
    relative_pace: Mapped[float] = mapped_column(Numeric(5,1))
    offensive_rating: Mapped[float] = mapped_column(Numeric(5,1))
    relative_offensive_rating: Mapped[float] = mapped_column(Numeric(5,1))
    top_win_shares_player: Mapped[str] = mapped_column(String(100))
    games: Mapped[int] = mapped_column()
    minutes_played: Mapped[int] = mapped_column()
    field_goals: Mapped[int] = mapped_column()
    field_goals_attempt: Mapped[int] = mapped_column()
#    field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    three_point_field_goals: Mapped[int] = mapped_column()
    three_point_field_goal_attempt: Mapped[int] = mapped_column()
#    three_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    two_point_field_goals: Mapped[int] = mapped_column()
    two_point_field_goal_attempt: Mapped[int] = mapped_column()
#   two_point_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    effective_field_goals_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    free_throws: Mapped[int] = mapped_column()
    free_throws_attempt: Mapped[int] = mapped_column()
#    free_throws_percentage: Mapped[float] = mapped_column(Numeric(5, 3))
    offensive_rebounds: Mapped[int] = mapped_column()
    defensive_rebounds: Mapped[int] = mapped_column()
#    total_rebounds: Mapped[int] = mapped_column()
    assists: Mapped[int] = mapped_column()
    steals: Mapped[int] = mapped_column()
    blocks: Mapped[int] = mapped_column()
    turnovers: Mapped[int] = mapped_column()
    points: Mapped[int] = mapped_column()
    personal_fouls: Mapped[int] = mapped_column()



# --------------------------------------------------------------------------------------------------

class MvpVotes(Base):
    __tablename__ = 'MVP_votes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'))
    season_id: Mapped[int] = mapped_column(ForeignKey('seasons.season_id'))
    rank: Mapped[int] = mapped_column()
    first_place_votes: Mapped[int] = mapped_column()
    points_won: Mapped[int] = mapped_column()
    points_max: Mapped[int] = mapped_column()
    share: Mapped[float] = mapped_column(Numeric(5,3))
#    win_shares: Mapped[float] = mapped_column(Numeric(5,1))
#    win_shares_per_48: Mapped[float] = mapped_column(Numeric(5,3))
#    games: Mapped[int] = mapped_column()
#    minutes_played_per_game: Mapped[float] = mapped_column(Numeric(5,1))
#    points_per_game: Mapped[float] = mapped_column(Numeric(5,1))
#    total_rebounds_per_game: Mapped[float] = mapped_column(Numeric(5,1))  # I think the naming is weird
#    assists_per_game: Mapped[float] = mapped_column(Numeric(5,1))
#    steals_per_game: Mapped[float] = mapped_column(Numeric(5,1))
#    blocks_per_game: Mapped[float] = mapped_column(Numeric(5,1))
#    field_goal_percentage: Mapped[float] = mapped_column(Numeric(5,3))
#    three_point_field_goal_percentage: Mapped[float] = mapped_column(Numeric(5,3))
#    free_throw_percentage: Mapped[float] = mapped_column(Numeric(5,3))

# --------------------------------------------------------------------------------------------------

class Champ(Base):
    __tablename__ = "champ"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.season_id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))