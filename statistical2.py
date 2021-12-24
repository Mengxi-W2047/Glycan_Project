#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: WMX
# Date: 20211224
# This tool supports txt/excel/csv format file and will output the count number of glycoprotein, glycopeptide, glycosite and glycan.


import pandas as pd
from tkinter.filedialog import askopenfilename

fileName = askopenfilename()
print(fileName)
if fileName.split(".")[-1] == "txt":
    df = pd.read_table(fileName, header=0)
elif fileName.split(".")[-1] == "xlsx":
    df = pd.read_excel(fileName, header=0)
elif fileName.split(".")[-1] == "csv":
    df = pd.read_csv(fileName, header=0)
else:
    print("The file format is wrong.")

protein_list = []
site_list = []
glycopep_list = []
glycan_list = []

for i in range(len(df)):
    if df["Glycan(H,N,A,G,F,pH)"][i] not in glycan_list:
        glycan_list.append(df["Glycan(H,N,A,G,F,pH)"][i])
    if df["Proteins"][i]+str(df["ProSites"][i])+df["Glycan(H,N,A,G,F,pH)"][i] not in glycopep_list:
        glycopep_list.append(df["Proteins"][i]+str(df["ProSites"][i])+df["Glycan(H,N,A,G,F,pH)"][i])
    if df["Proteins"][i]+str(df["ProSites"][i]) not in site_list:
        site_list.append(df["Proteins"][i]+str(df["ProSites"][i]))
    if df["Proteins"][i] not in protein_list:
        protein_list.append(df["Proteins"][i])

print("Glycoprotein: ", len(protein_list))
print("Glycosite: ", len(site_list))
print("Glycopeptide: ", len(glycopep_list))
print("Glycan: ", len(glycan_list))