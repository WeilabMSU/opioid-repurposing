# Machine-learning Analysis of Opioid Use Disorder Informed by MOR, DOR, KOR, NOR and ZOR-Based Interactome Networks

---
This script is for the paper "Machine-learning Analysis of Opioid Use Disorder Informed by MOR, DOR, KOR, NOR and ZOR-Based Interactome Networks". With the script, machine-learning regression model based on natural language processing (NPL) method can be built.

## Requirements

OS Requirements
- CentOS Linux 7 (Core)

Python Dependencies
- setuptools (>=18.0)
- python (>=3.7)
- pytorch (>=1.2)
- rdkit (2020.03)
- biopandas (0.2.7)
- numpy (1.17.4)
- scikit-learn (0.23.2)
- scipy (1.5.2)
- pandas (0.25.3)
- cython (0.29.17)


## Download the repository
Download the repository from Github
```shell
# download repository by git
git clone https://github.com/WeilabMSU/OUD_PPI.git
```
## Install the pretrained model for molecular fingerprint generation

The feature generation follows the work "Extracting Predictive Representations from Hundreds of Millions of Molecules" by Dong Chen, Jiaxin Zheng, Guo-Wei Wei, and Feng Pan." The pretrained model in their work was built based on transformer NPL techniques and is utilized to generate molecular features here. In addition, Extended-connectivity fingerprints (ECFPs) is utilized.

Download and install the pretrained model under the downloaded OUD_PPI folder.

```shell
cd repurposing_OUD
bash install-transformer.sh
```

## Generate molecular fingerprints
The input for our feature generation model is *.smi file, which stores molecules of SMILES format. The command below can be used to generate transformer-based molecular fingerprints. An example *.smi file is given as MOR.smi

```python
cd OUD_PPI
python fp-generation.py --path-to-smi MOR.smi
```
The generated features are saved in the folder "features".

## Build GBDT model with the transformer-based molecular fingerprints
Below is the script used to build gradient boosting decision tree (model) machine-learning model using the generated transformer-based molecular fingerpints. An example feature file and label file are given as MOR.npy and MOR.csv. The generated machine-learning model is save in the "path-models" folder.

```python
cd OUD_PPI
python build-GBDT-regression.py --feature_path features/MOR.npy --label_path MOR.csv --save_model_name MOR
```

## Reference

1. Machine-learning Analysis of Opioid Use Disorder Informed by MOR, DOR, KOR, NOR and ZOR-Based Interactome Networks, in print (2023).

2. Dong Chen, Jiaxin Zheng, Guo-Wei Wei, and Feng Pan. Extracting predictive representations from
hundreds of millions of molecules. The Journal of Physical Chemistry Letters, 12(44):10793–10801, 2021.

## License
All codes released in this study is under the MIT License.
