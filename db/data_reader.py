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


def load_jobcards(filename="workDetails.csv"):
    records = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['panchayatName'] not in records:
                records[row['panchayatName']] = {}
            if row['jobcard'] not in records[row['panchayatName']]:
                records[row['panchayatName']][row['jobcard']] = {
                    'count': 0,
                    'dates': set()
                }
            records[row['panchayatName']][row['jobcard']]['count'] += 1
            records[row['panchayatName']][row['jobcard']]['dates'].add(
                row['dateTo'])

    firebase_conn = firebase.FirebaseApplication(
        'https://libtech-backend.firebaseio.com/', None)
    for panchayat_name in records:
        for jobcard in records[panchayat_name]:
            records[panchayat_name][jobcard]['earliest_date'] = \
                min(records[panchayat_name][jobcard]['dates'])
            records[panchayat_name][jobcard]['latest_date'] = \
                max(records[panchayat_name][jobcard]['dates'])
            print (panchayat_name, jobcard,
                   records[panchayat_name][jobcard]['earliest_date'],
                   records[panchayat_name][jobcard]['latest_date'],
                   records[panchayat_name][jobcard]['count'])
            new_record = {
                'num_transactions': records[panchayat_name][jobcard]['count'],
                'earliest_date':
                records[panchayat_name][jobcard]['earliest_date'],
                'latest_date': records[panchayat_name][jobcard]['latest_date'],
            }
            try:
                result = firebase_conn.put('/jobcards',
                                           '{0}/{1}'.format(
                                              panchayat_name,
                                              jobcard.replace('/', '_')),
                                           new_record)
            except Exception as e:
                print ("\n\n\n\nWATCH!!!!!")
                print (e)
            print (result)


def load_transactions(filename="workDetails.csv"):
    records = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['panchayatName'] not in records:
                records[row['panchayatName']] = {}
            if row['jobcard'] not in records[row['panchayatName']]:
                records[row['panchayatName']][row['jobcard']] = []
            records[row['panchayatName']][row['jobcard']].append(row)

    firebase_conn = firebase.FirebaseApplication(
        'https://libtech-backend.firebaseio.com/', None)
    for panchayat_name in records:
        for jobcard in records[panchayat_name]:
            for i, record in enumerate(records[panchayat_name][jobcard]):
                jc = jobcard.replace('/', '_')
                print (jc + ':{}'.format(i + 1), record)
                try:
                    result = firebase_conn.put('/transactions',
                                               '{0}/{1}'.format(
                                                   jc,
                                                   jc + ':{}'.format(i + 1)),
                                               record)
                except Exception as e:
                    print (e)
                print (result)
