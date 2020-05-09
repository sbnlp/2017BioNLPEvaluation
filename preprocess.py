"""First step is to preprocess corpora that is stored inside the data directory.
 To do this we use class Preprocess that comes with TEES.
 It changes .tar.gz archives downloaded from ST website into interaction XML.
 Omiting step 'NER' is crucial to not have duplicated ids from BANNER.
"""
import os
from os.path import isfile, join
from tees.Detectors.Preprocessor import Preprocessor


data_directory = 'data/' # relative path
current_dir = os.getcwd()

files = [f for f in os.listdir(data_directory) if isfile(join(data_directory, f))]

omit_banner = 'NER'
preprocessor = Preprocessor()

for file in files:
    if file.endswith(('-test.tar.gz', '-devel.tar.gz', '-train.tar.gz')):
        dataset_name = file[:-7] # without .tar.gz
        print dataset_name
        input = current_dir + "/" + data_directory + file
        output = current_dir + "/" + data_directory + dataset_name + '/' + dataset_name + '.xml'
        preprocessor.process(source=input, output=output, omitSteps = omit_banner)
