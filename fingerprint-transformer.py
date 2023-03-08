import os
from rdkit import Chem
import argparse
import numpy as np
import pickle

parser = argparse.ArgumentParser(description='generated transformer embedding')
parser.add_argument('--dataset', type=str,help='input the path to your SMILES file')
args = parser.parse_args()

dataset = args.dataset

# generate transformer features based on given SMILES file

class ligand_Featurization():
    def __init__(self,model_select='chembl27_512'):
        self.model_path = 'PretrainModels/'+model_select
        self.dict_file = "%s/dict.txt"%(self.model_path)
        self.generate = 'PretrainModels/bt_pro/generate_bt_fps_mean.py'

    def process(self,smi_file,feature_file):

        cwd = "python %s  --model_name_or_path %s \
        --checkpoint_file checkpoint_best.pt  \
        --data_name_or_path  %s  --dict_file %s \
        --target_file %s  --save_feature_path %s\n"%(self.generate, self.model_path,
        self.model_path, self.dict_file, smi_file, feature_file)

        os.system(cwd)

models=['chembl27_512','chembl27_pubchem_512','chembl27_pubchem_zinc_512']
model_select=models[0]

L = ligand_Featurization(model_select)

SMILES = open('%s.smi'%(dataset)).read().splitlines()
fw = open('temp-transformer.smi','w')
for smi in SMILES:
    smi_cano = Chem.MolToSmiles(Chem.MolFromSmiles(smi), canonical=True)
    try:
        print(smi_cano,file=fw)
    except:
        print(smi,file=fw)
fw.close()

if not os.path.exists('features'):
    os.mkdir('features')

feature_path = 'features/%s.npy'%(dataset)
L.process('temp-transformer.smi', feature_path)

os.system('rm temp-transformer.smi')

