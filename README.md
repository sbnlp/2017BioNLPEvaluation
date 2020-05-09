# 2017BioNLPEvaluation

This repository contains code and data for the following article:

Wojciech Kusa, Michael Spranger. [_External Evaluation of Event Extraction Classifiers for Automatic Pathway Curation: An extended study of the mTOR pathway._](https://www.aclweb.org/anthology/W17-2331.pdf) In Proceedings of the 2017 Workshop on Biomedical Natural Language Processing (BioNLP 2017), pages 247–256. Association for Computational Linguistics, 2017.


## 1. Installation

This software was tested on Ubuntu 16.04

### 1.1 Python

This project requires Python 2.7.

```console
$ conda create -n bioNLP2017 python=2.7
$ conda activate bioNLP2017
(bioNLP2017) $ pip install -r requiremnts.txt
```

### 1.2 TEES

This project uses [_Turku Event Extraction System (TEES)_](https://github.com/jbjorne/TEES) in version 2.2.1. To properly install all dependencies (classifiers, models, corpora and preprocessing tools) you need to run

```console
(bioNLP2017) $ python tees/configure.py
```

TEES installs the following dependencies:
- GENIA Sentence Splitter
- BANNER named entity recognizer
- BLLIP parser
- Stanford Parser

Stanford parser and BLLIP requires `java`, `g++`, `flex` and `ruby`. Use the following command to install them if they are missing on your system:

```console
(bioNLP2017) $ sudo apt-get install g++ ruby flex default-jre
```

After succesfull installation of TEES you need to export the path

```console
(bioNLP2017) $ export TEES_SETTINGS=/home/${USER}/.tees_local_settings.py
```


## 2. Data

### 2.1 Training data

Training datasets were created using three different sources:
 - _ANN_ - consists of 60 abstracts of scientific papers from Pubmed database related to the mTORpathway map.
 - _GE11_ consists of 908 abstracts and full texts of scientific papers used in BioNLP ST 2011 GENIA Event Extraction task
 - _PC13_ consists of 260 abstracts of scientific papers used in BioNLP ST 2013 Pathway Curation task

All train datasets are stored in `data/` directory

1. `data/GE11-train.tar.gz` - standalone GE11
2. `data/GE11_mTOR-ann-train.tar.gz` -  GE11+ANN - combined GE11 and ANN
3. `data/GE11_PC13_mTOR-ann-train.tar.gz` - GE11+PC13+ANN - combined GE11, PC13 and ANN
4. `data/PC13_mTOR-ann-train.tar.gz` - PC13+ANN - combined PC13 and ANN

For hyperparameter optimization of all classifiers _"GE11-Devel BioNLP ST2011"_ dataset was used.

### 2.2 Test data

Test data consists of 449 full text papers mentioned in the mTOR pathway map. Original paper pdfs were downloaded and translated into raw txt files using CERMINE.

Test data in a format of preprocessed txt files can be downloaded from [here](https://www.dropbox.com/sh/6rvjss2c4g29ifo/AADerqgF0sN6AgRV-eUh5vHPa?dl=0). Documents should be extracted to: `data/evaluation_mTOR_full/` directory.


## 3. Training and testing event extraction models

First you need to preprocess training datasets:

```console
(bioNLP2017) $ python preprocess.py
```

To train event extraction model run:

```console
(bioNLP2017) $ python train.py \
--output_path results/GE11-SVM/ \
--classifier svm \
--train_data data/GE11-train/GE11-train.xml
```

To run predictions on mTOR papers with the model trained from the previous step:

```console
(bioNLP2017) $ python predict.py \
--model_path results/GE11-SVM/ \
--input_data data/evaluation_mTOR_full/ \
--output_path results/GE11-SVM/evaluation_mTOR_full/
```

If you don't want to train your models you can use models included in TEES, e.g.:

```console
(bioNLP2017) $ python predict.py \
--model_path /home/${USER}/.tees/models/GE11-devel \
--input_data data/evaluation_mTOR_full/ \
--output_path results/GE11/SVM/evaluation_mTOR_full/
```

### 3.1 Event extraction results

Results from all 17 pretrained models from the paper can be downloaded from [here](https://www.dropbox.com/sh/7gkxjad99dixdsu/AAD0G_O75ImkrhHIvzoUn7Gwa?dl=0).


## 4. Evaluation

Evaluation was done with scripts from [sbnlp/mTOR-evaluation](https://github.com/sbnlp/mTOR-evaluation).
