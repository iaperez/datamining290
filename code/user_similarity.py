from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re
import itertools
WORD_RE = re.compile(r"[\w']+")


# I reviewed this explanation
# http://aimotion.blogspot.com/2012/08/introduction-to-recommendations-with.html
# to understand the flow of information in mrjob
# I had no idea how to yield a set like <key,list>
#


class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

########
#     
# for each user, i'm calculating the total of his/her reviews
# get_business_per_user
# then, I join that total with the user_id: (userid, total_reviews)
#
########    
    def get_business_per_user(self, _, record):
        """Taking in a record, and extract business_id and user_id"""
        if record['type'] == 'review':
            yield [record['user_id'],record['business_id']]

    def group_business_per_user(self, user_id, business_id):
        #unique reviews per users
        business_per_users = set(business_id)  # set() uniques an iterator  
        yield [user_id, [len(business_per_users),list(business_per_users)]]

########
#     
# for each business, i'm calculating a bag with the all the tuples (user,total) that
# reviewed that business
# 
########    

    def get_users_per_business(self, user_id, values):
        #getting the users+total per business, 
        total_reviews_per_user,business_per_user= values
        for business in business_per_user:
            yield business,(user_id,total_reviews_per_user)

    def group_users_per_business(self,business_id, user_data):
        unique_users_per_business = set(tuple(x) for x in user_data)
        yield(business_id, list(unique_users_per_business))

########
#     
# for each business, i'm calculating a bag with the all the (user,total) that
# reviewed that business
# 
######## 

    def pairs_of_users(self, business_id, users):
        for pair in itertools.combinations(users,2):
            if ((pair[0][1]/pair[1][1])<=2 and (pair[0][1]/pair[1][1])>=0.5):
                yield [pair, 1]

    def finish_jaccard(self,pair_of_users,count_of_pair):
        total =  sum(count_of_pair)
        user_a_rvs= pair_of_users[0][1]
        user_b_rvs= pair_of_users[1][1]
        jaccard = float(total)/float(user_a_rvs+user_b_rvs-total)
        if jaccard>=0.5:
            yield [pair_of_users,jaccard]


    def steps(self):
        return [self.mr(self.get_business_per_user, self.group_business_per_user),
                self.mr(self.get_users_per_business, self.group_users_per_business),
                self.mr(self.pairs_of_users,self.finish_jaccard)]

if __name__ == '__main__':
    UserSimilarity.run()
