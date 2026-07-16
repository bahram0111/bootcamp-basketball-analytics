from crud import create_player
from session import get_session


with get_session() as session:

    create_player(
        session,
        # player_data from scrape
    )