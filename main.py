import import_data
import apriori as apr
import association_rules_division as ard
import association_rules_pure_python as aprpp
from additional_functions import create_converted_r_matrix
import fuzzy_curves as fc
import recommend as re
import visualizations as vs
import numpy as np

# read data
data = import_data.ImportData('smoker')
data.import_data()
# data.import_movies_genres()

#choose fuzzy curves class
curves = fc.Curves1(data.min_score, data.max_score, 0.2, 0.45, 0.55, 0.8)
#
# # create fuzzy association rules
conv_r_matrix = create_converted_r_matrix(data.r_matrix, curves)
t_matrix = data.t_matrix

# apriori1 = apr.Apriori(conv_r_matrix, curves.Names, 0.0052)
# freq1, sup1 = apriori1.apriori()
#
# apriori2 = ard.AssociationRules(conv_r_matrix, 20, curves.Names, min_support=0.0000001, min_confidence=0.4)
# freq2, sup2 = apriori2.main()

# apriori3 = aprpp.AssociationRules(conv_r_matrix, curves.Names, 0.0052)
# freq3, sup3 = apriori3.apriori()


# rules1 = apriori1.algorithm_main()
# rules2 = apriori2.algorithm_main()

recomm = re.Recommend(conv_r_matrix)
# f = recomm.recommend_to_user(rules2, 11)
recomm_score = recomm.main_recommend(20, curves.Names, test_size=0.3, cross_num=5, min_support=0.0000000001, min_confidence=0.000004)


pass
