import pickle
import json
import pytrec_eval

def eval (x,y,z):
    with open('corrections_at_k10_0-15.pkl', 'rb') as f:
        correct1 = pickle.load(f)
    with open('golden_standard_at_k10_0-15.pkl', 'rb') as f:
        gs1 = pickle.load(f)

    with open('corrections_at_k10-15-25.pkl', 'rb') as f:
        correct2 = pickle.load(f)
    with open('golden_standard_at_k-10-15-25.pkl', 'rb') as f:
        gs2 = pickle.load(f)

    with open('corrections_at_k10_25-35.pkl', 'rb') as f:
        correct3 = pickle.load(f)
    with open('golden_standard_at_k10_25-35.pkl', 'rb') as f:
        gs3 = pickle.load(f)

    with open('corrections_at_k10_35-36.pkl', 'rb') as f:
        correct4 = pickle.load(f)
    with open('golden_standard_at_k10_35-36.pkl', 'rb') as f:
        gs4 = pickle.load(f)

    correct1.update(correct2)
    correct1.update(correct3)
    correct1.update(correct4)

    gs1.update(gs2)
    gs1.update(gs3)
    gs1.update(gs4)

    evaluator = pytrec_eval.RelevanceEvaluator(correct1, {x, y, z})
    succ_1 = []
    succ_5 = []
    succ_10 = []

    sum_succ_1 = 0
    sum_succ_5 = 0
    sum_succ_10 = 0

    avg_succ_1 = 0
    avg_succ_5 = 0
    avg_succ_10 = 0

    with open("myfile.json", "w") as j:
        j.write(json.dumps(evaluator.evaluate(gs1)))
    with open("myfile.json", "r") as j:
        mydata = json.load(j)

        for key, value in mydata.items():
            succ_1.append(value['success_1'])
            succ_5.append(value['success_5'])
            succ_10.append(value['success_10'])
            print()
    for i in range(len(succ_1)):
        sum_succ_1 = sum_succ_1 + succ_1[i]
        #   print(sum_succ_1)
        sum_succ_5 = sum_succ_5 + succ_5[i]
        #  print(sum_succ_5)
        sum_succ_10 = sum_succ_10 + succ_10[i]
    # print(sum_succ_10)

    avg_succ_1 = sum_succ_1 / len(succ_1)
    avg_succ_5 = sum_succ_5 / len(succ_5)
    avg_succ_10 = sum_succ_10 / len(succ_10)

    print("succ_1:", avg_succ_1, len(succ_1), "\n" "succ_5:", avg_succ_5, len(succ_5), "\n" "succ_10: ", avg_succ_10,
          len((succ_10)))

