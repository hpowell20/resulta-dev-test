import argparse

from helpers.request_utils import process_results
from rest import rankings, scores


if __name__ == '__main__':
    # Read input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-sd', '--start_date', required=True,
                        help='The query date range start')
    parser.add_argument('-ed', '--end_date', required=True,
                        help='The query date range end')
    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date

    try:
        # Retrieve the team rankings list
        rankings_dict = rankings.get_rankings()

        # Retrieve the raw score results
        start_date_obj, end_date_obj, scores_dict = scores.get_scores(start_date, end_date)

        # Find all the results between the start and end dates
        print(process_results(scores_dict, rankings_dict, start_date_obj, end_date_obj))
    except Exception as e:
        print(e)
