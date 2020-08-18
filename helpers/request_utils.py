import pandas as pd

from datetime import datetime
from dateutil.relativedelta import relativedelta

from helpers.date_utils import get_date_object, get_formatted_date
from helpers.number_utils import convert_string_to_float
from rest.constants import EVENT_DATE_FORMAT, EVENT_TIME_FORMAT

KEY_NAME_DATA = 'data'
KEY_NAME_COLUMNS = 'columns'
OUTPUT_DATE_FORMAT = '%d-%m-%Y'
OUTPUT_TIME_FORMAT = '%H:%M'


def process_results(scores: dict, rankings: dict, start_date: datetime, end_date: datetime):
    # Retrieve the team rankings list
    teams_list = rankings.get(KEY_NAME_DATA)
    teams_lookup = pd.DataFrame(teams_list,
                                columns=rankings.get(KEY_NAME_COLUMNS),
                                index=[x['team_id'] for x in teams_list])

    response_json = []

    # Process events for each date in the query range
    while start_date <= end_date:
        curr_date = get_formatted_date(start_date, EVENT_DATE_FORMAT)
        scores_data = scores.get(curr_date)
        if KEY_NAME_DATA in scores_data:
            data = scores_data.get(KEY_NAME_DATA)
            for key, value in data.items():
                event_details = data.get(key)
                event_item = create_event_item(event_details, teams_lookup)
                response_json.append(event_item)

        start_date += relativedelta(days=1)

    return response_json


def create_event_item(event_details: dict, teams_lookup: pd.DataFrame):
    # Set the event date details
    is_valid, event_date = get_date_object(event_details.get('event_date'),
                                           f"{EVENT_DATE_FORMAT} {EVENT_TIME_FORMAT}")

    # Read in the details from the rankings list
    away_team_id = event_details.get('away_team_id')
    away_team = teams_lookup.loc[away_team_id]
    home_team_id = event_details.get('home_team_id')
    home_team = teams_lookup.loc[home_team_id]

    # Create the event item
    return {
        'event_id': event_details.get('event_id'),
        'event_date': get_formatted_date(event_date, OUTPUT_DATE_FORMAT),
        'event_time': get_formatted_date(event_date, OUTPUT_TIME_FORMAT),
        'away_team_id': event_details.get('away_team_id'),
        'away_nick_name': event_details.get('away_nick_name'),
        'away_city': event_details.get('away_city'),
        'away_rank': away_team.get('rank'),
        'away_rank_points': convert_string_to_float(away_team.get('adjusted_points')),
        'home_team_id': home_team_id,
        'home_nick_name': event_details.get('home_nick_name'),
        'home_city': event_details.get('home_city'),
        'home_rank': home_team.get('rank'),
        'home_rank_points': convert_string_to_float(home_team.get('adjusted_points'))
    }
