import argparse
import os

import tees.classify


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str,
                        default='results/GE11-SVM/model-test')
    parser.add_argument("--input_data", type=str, help="this should be relative path",
                        default='data/evaluation_mTOR_full/')
    parser.add_argument("--output_path", type=str, help="this should be relative path",
                        default='results/GE11-SVM/evaluation_mTOR_full/')

    args = parser.parse_args()

    print(args.model_path)
    print(args.input_data)
    print(args.output_path)

    current_dir = os.getcwd()

    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    bioNLPSTParams = {"scores" : False,
                      "convert" : True
    }

    with open("data/pubmed-ids.txt") as fp:
        pubmed_ids = [x.strip() for x in fp.readlines()]

    for pubmed_id in pubmed_ids:
        input_file = current_dir + "/" + args.input_data + "/" + pubmed_id + ".ascii.cermxml.txt"
        output = current_dir + "/" + args.output_path + "/" + pubmed_id + "/"

        print input_file
        if os.path.exists(input_file):
            tees.classify.classify(model=args.model_path,
                                   input=input_file,
                                   output=pubmed_id,
                                   workDir=output,
                                   bioNLPSTParams=bioNLPSTParams)
        else:
            print "file not exists: ", input_file
