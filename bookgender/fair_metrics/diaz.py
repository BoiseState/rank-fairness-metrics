# Expected Exposure ee_metrics
# Currently: EE-L, EE-R, EE-D, Group fairness as well

import pandas as pd
import numpy as np

    
    #To use these metrics on recommendations, users are considered as sequences.
    #To use thse metrics on IR tasks, runs for same query are used as sequences
    
    
# Group Fairness -- Computes EE-D, EE-L, EE-R
def ee_for_ds(data, test, group_info, pweight):
    """
    Compute Expected Exposure metrics (EEL, EED, EER).

    Args:
        data(pandas.DataFrame):
            Data frame of recommendations (all rankings for a system).
        test(pandas.DataFrame):
            The test data.
        group_info(GroupInfo):
            The group info object.
        pweight:
            The position weighting object.
    """
    def groupwise(udf, group):
        exp = pweight(udf)
        #mat = udf[[group.major, group.minor]]
        mat = udf[[group.major, group.minor, group.unknown]]
        return mat.T @ exp

    def group_ideal(udf, group):
        exp = pweight.ideal(udf['rating'])
        #return udf[[group.major, group.minor]].T @ exp
        return udf[[group.major, group.minor, group.unknown]].T @ exp
    try:
        sys = data.groupby('user').apply(groupwise, group=group_info)
        sys = sys.mean()

        tgt = test.groupby('user').apply(group_ideal, group=group_info)
        tgt = tgt.mean()
    except:
        sys = data.groupby('sequence').apply(groupwise, group=group_info)
        sys = sys.mean()
        qid = data['qid'].unique()[0]
        test_qid = test.loc[test['qid']==qid]

        tgt = group_ideal(test_qid, group=group_info)
        
    diff = sys - tgt

    return pd.Series({
        'EEL': np.dot(diff, diff),
        'EED': np.dot(sys, sys),
        'EER': 2 * np.dot(sys, tgt)
    })
