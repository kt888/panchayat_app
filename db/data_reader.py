import csv
from firebase import firebase


def load_records(filename="workDetails.csv"):
	records = {}
	with open(filename) as f:
		reader = csv.DictReader(f)
		for row in reader:
			if row['panchayatName'] not in records:
				records[row['panchayatName']] = {}
			if row['jobcard'] not in records[row['panchayatName']]:
				records[row['panchayatName']][row['jobcard']] = []
			records[row['panchayatName']][row['jobcard']].append(row)
	from firebase import firebase
	firebase = firebase.FirebaseApplication('https://libtech-app.firebaseio.com', None)
	for pan, values in records.iteritems():
		for jc, data in values.iteritems():
			dat = {'num_transactions': len(data), 'data': data}
			result = firebase.post('/data/{0}/{1}'.format(pan, jc), dat)


load_records()
