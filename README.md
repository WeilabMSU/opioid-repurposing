# Machine-learning Repurposing of DrugBank Compounds for Opioid Use Disorder

---
This script is for the paper "Machine-learning Repurposing of DrugBank Compounds for Opioid Use Disorder". With the script, binding affinities of molecular compounds on MOR, KOR, DOR, and hERG are be predicted.

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
git clone https://github.com/WeilabMSU/opioid-repurposing.git
```
## Install the pretrained model for molecular fingerprint generation

The feature generation follows the work "Extracting Predictive Representations from Hundreds of Millions of Molecules" by Dong Chen, Jiaxin Zheng, Guo-Wei Wei, and Feng Pan." The pretrained model in their work was built based on transformer NPL techniques and is utilized to generate molecular features. In addition, Extended-connectivity fingerprints (ECFPs) is utilized.

Download and install the pretrained model under the downloaded opioid-repurposing folder.

```shell
cd opioid-repurposing
bash install-transformer.sh
```

## Generate molecular fingerprints
The input for our feature generation model is *.smi file, which stores molecules of SMILES format. The command below can be used to generate transformer-based and ECFPs molecular fingerprints. An example test.smi file is given.

```python
cd opioid-repurposing
python fingerprint-transformer.py --dataset test
python fingerprint-ecfp.py --dataset test
```
The generated features are saved in the folder "features".

## Download the GBDT models built with two types of molecular fingerprints. 
Download the trained regression models for predicting binding affiinties on MOR, KOR, DOR, and hERG.

```shell
cd opioid-repurposing
wget https://weilab.math.msu.edu/Downloads/models-opioid.zip
unzip models-opioid.zip
```

## Use GBDT models to predict the binding affinities of the molecular compounds on proteins including MOR,KOR,DOR, and hERG.
Below is the script used to predict the binding affinities using models based on transformer and ECFP fingerprints. The prediction results can be found in "prediction" folder.

```python
cd opioid-repurposing
python predictor-GBDT-regression.py --dataset test
```

## Reference

1. Machine-learning Repurposing of DrugBank Compounds for Opioid Use Disorder, in print (2023).

2. Dong Chen, Jiaxin Zheng, Guo-Wei Wei, and Feng Pan. Extracting predictive representations from
hundreds of millions of molecules. The Journal of Physical Chemistry Letters, 12(44):10793–10801, 2021.

## License
All codes released in this study is under the MIT License.
