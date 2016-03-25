import csv
from cleandictreader import CleanDictReader
from tripleutils import print_triple_literal

COMPANY_URI = 'http://dnb.com/duns/%s'

with open("sample.csv") as csv_in:
    reader = CleanDictReader(csv_in, delimiter='|')
    for row in reader:
        subject_duns =  row['subj_duns_nbr']
        company_uri = COMPANY_URI % subject_duns
        del row['subj_duns_nbr']

        for key in row.keys():
            predicate = 'http://dnb.com/company/beneficial-ownership-attributes/' + key
            print_triple_literal(company_uri, predicate, row[key])


