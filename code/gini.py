#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""
from collections import defaultdict
from collections import Counter

import fileinput
import csv

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
candidates =  defaultdict(Counter)
zipcodes =  defaultdict(Counter)

############### Read through files
############### I decided to cleanup the zipcodes, taking only the first 5 digits
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        candidates[row[cand_nm]][row[contbr_zip][:5]]+=1
        zipcodes[row[contbr_zip][:5]][row[cand_nm]]+=1

# for gini calculations, the total of contrbutors in the dataset
totalcontributors = sum([sum(x.values()) for x in candidates.itervalues()]);


probs_per_candidate =  defaultdict(float)
for candidate in candidates.iterkeys():
    probs_per_candidate[candidate]=float(sum(candidates[candidate].values()))/float(totalcontributors)

def gini_per_zipcode(dict_of_contributors):
    total_contributors_per_zip=sum(dict_of_contributors.values())
    probs_per_candidate_in_zipcode = defaultdict(float)
    for candidate in dict_of_contributors.keys():
        probs_per_candidate_in_zipcode[candidate]=float(dict_of_contributors[candidate])/float(total_contributors_per_zip) 
    return 1-sum(probs**2 for probs in probs_per_candidate_in_zipcode.values())

###
# TODO: calculate the values below:
gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

gini = 1 - sum(probs**2 for probs in probs_per_candidate.values())
split_gini = sum(sum(x.values())*gini_per_zipcode(x)/totalcontributors for x in zipcodes.values())

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
