from rdkit.Chem import rdmolfiles
from rdkit.Chem import AllChem
from rdkit import Chem
import argparse
import os

parser = argparse.ArgumentParser(description='generated transformer embedding')
parser.add_argument('--dataset', type=str,help='input the path to your SMILES file')
args = parser.parse_args()

dataset = args.dataset

def fp_ecfp4():

    SMILES = open('%s.smi'%(dataset)).read().splitlines()
    nsmi = len(SMILES)

    fp_dir = 'features'
    if not os.path.exists(fp_dir):
        os.mkdir(fp_dir)

    subdir_smi = 'temp-ecfp'
    if not os.path.exists(subdir_smi):
        os.mkdir(subdir_smi)
    for ismi,smi in enumerate(SMILES):
        with open('%s/%s-%d.smi'%(subdir_smi,dataset,ismi),'w') as fw:
            smi_cano = Chem.MolToSmiles(Chem.MolFromSmiles(smi), canonical=True)
            print(smi_cano,file=fw,end='')

    bits=2048
    fo=open("%s/%s-ecfp4.csv"%(fp_dir,dataset),"w")
    for ismi in range(nsmi):
        suppl = rdmolfiles.SmilesMolSupplier('%s/%s-%d.smi'%(subdir_smi,dataset,ismi),titleLine=False,delimiter='\t')
        fp = AllChem.GetMorganFingerprintAsBitVect(suppl[0],3,nBits=bits)
        
        for i in range(0,bits):
            dt=int(fp.GetBit(i))
            if(i<bits-1):
                print("%s, "%dt,end="",file=fo)
            else:
                print("%s"%dt,file=fo)

    fo.close()
    
    os.system('rm -r %s'%(subdir_smi))

fp_ecfp4()
