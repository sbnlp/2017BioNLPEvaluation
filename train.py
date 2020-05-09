import argparse
import getpass
import os

import tees.train


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_path", type=str,
                        default='results/GE11-SVM/')
    parser.add_argument("--classifier", default='svm', nargs='?',
                        choices=['svm', 'rf', 'dt', 'mnnb', 'mlp'])
    parser.add_argument("--train_data", type=str,
                        default=None)

    args = parser.parse_args()

    tees_path = "/home/" +  getpass.getuser() + "/.tees/corpora/"
    inputFiles={"train": tees_path + "GE11-train.xml",
                "devel": tees_path + "GE11-devel.xml",
                "test": tees_path + "GE11-test.xml"}
    if args.train_data:
        inputFiles['train'] = os.getcwd() + "/" + args.train_data

    models = {"devel": "model-devel", "test": "model-test"}
    parse = "McCC"
    detector = "Detectors.EventDetector"

    if args.classifier == "svm":
        model = None # use TEES defaults
        recallAdjustParams = None
    elif args.classifier == "rf":
        model = "TEES.classifier=ScikitClassifier:scikit=ensemble.RandomForestClassifier:n_estimators=5,10,50"
        recallAdjustParams = '1'
    elif args.classifier == "mlp":
        model = "TEES.classifier=ScikitClassifier:scikit=neural_network.MLPClassifier"
        recallAdjustParams = '1'
    elif args.classifier == "dt":
        model = "TEES.classifier=ScikitClassifier:scikit=tree.DecisionTreeClassifier"
        recallAdjustParams = '1'
    elif args.classifier == "mnnb":
        model = "TEES.classifier=ScikitClassifier:scikit=naive_bayes.MultinomialNB"
        recallAdjustParams = '1'

    print("starting training")
    tees.train.train(output=args.output_path,
                     models=models,
                     parse=parse,
                     detector=detector,
                     inputFiles=inputFiles,
                     classifierParams={"trigger": model,
                                       "edge": model,
                                       "unmerging": model,
                                       "modifiers": model,
                                       "recall": recallAdjustParams}
    )
    print("training finished")
