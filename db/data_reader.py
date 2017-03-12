import csv
from firebase import firebase


def load_panchayats(filename="workDetails.csv"):
    records = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['panchayatName'] not in records:
                records[row['panchayatName']] = {
                    'job_cards': set(),
                    'transactions': 0,
                    'dates': set()
                }
            records[row['panchayatName']]['job_cards'].add(row['jobcard'])
            records[row['panchayatName']]['transactions'] += 1
            records[row['panchayatName']]['dates'].add(row['dateTo'])
    firebase_conn = firebase.FirebaseApplication(
        'https://libtech-backend.firebaseio.com/', None)
    for panchayat_name in records:
        records[panchayat_name]['num_jobcards'] = \
            len(records[panchayat_name]['job_cards'])
        records[panchayat_name]['earliest_date'] = \
            min(records[panchayat_name]['dates'])
        records[panchayat_name]['latest_date'] = \
            max(records[panchayat_name]['dates'])
        new_record = {
            'num_jobcards': records[panchayat_name]['num_jobcards'],
            'earliest_date': records[panchayat_name]['earliest_date'],
            'latest_date': records[panchayat_name]['latest_date'],
            'transactions': records[panchayat_name]['transactions']
        }
        result = firebase_conn.put('/panchayats', panchayat_name,
                                   new_record)
        print (result)


load_panchayats()
