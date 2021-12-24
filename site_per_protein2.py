#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: WMX
# Date: 20211222

import pandas as pd
from tkinter.filedialog import askopenfilename


def site_per_protein():
    protein_list = []
    protein_dict = {}
    site_protein_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 10: 0}

    for i in range(len(df)):
        # print(i)
        if df["Proteins"][i] not in protein_list:
            protein_list.append(df["Proteins"][i])
            protein_dict[df["Proteins"][i]] = [df["ProSites"][i]]
        elif df["ProSites"][i] not in protein_dict[df["Proteins"][i]]:
            protein_dict[df["Proteins"][i]].append(df["ProSites"][i])
    # print(len(protein_list))

    for j in protein_dict:
        # print(j, len(protein_dict[j]))
        if len(protein_dict[j]) <= 4:
            site_protein_dict[len(protein_dict[j])] += 1
        elif 4 < len(protein_dict[j]) < 10:
            # print(len(protein_dict[j]))
            site_protein_dict[5] += 1
        elif len(protein_dict[j]) >= 10:
            # print(len(protein_dict[j]))
            site_protein_dict[10] += 1

    print("here is the site per protein distribution:")
    print(site_protein_dict)
    return


def glycan_per_site():
    site_list = []
    site_dict = {}
    glycan_site_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 10: 0, 20: 0}

    for i in range(len(df)):
        if df["Proteins"][i]+str(df["ProSites"][i]) not in site_list:
            site_list.append(df["Proteins"][i]+str(df["ProSites"][i]))
            site_dict[df["Proteins"][i]+str(df["ProSites"][i])] = [df["Glycan(H,N,A,G,F,pH)"][i]]
        elif df["Glycan(H,N,A,G,F,pH)"][i] not in site_dict[df["Proteins"][i]+str(df["ProSites"][i])]:
            site_dict[df["Proteins"][i]+str(df["ProSites"][i])].append(df["Glycan(H,N,A,G,F,pH)"][i])
    print(len(site_list))

    for j in site_dict:
        # print(j, len(site_dict[j]))
        if len(site_dict[j]) <= 4:
            glycan_site_dict[len(site_dict[j])] += 1
        elif 5 <= len(site_dict[j]) < 10:
            glycan_site_dict[5] += 1
        elif 10 <= len(site_dict[j]) < 20:
            glycan_site_dict[10] += 1
        elif 20 <= len(site_dict[j]):
            glycan_site_dict[20] += 1

    print("here is the glycan per site distribution:")
    print(glycan_site_dict)
    return


def glycan_size_distribution():
    glycopeptide_list = []
    glycan_size_dict = {5: 0, 6: 0, 8: 0, 10: 0, 13: 0, 16: 0}

    for i in range(len(df)):
        if df["Proteins"][i]+str(df["ProSites"][i])+df["Glycan(H,N,A,G,F,pH)"][i] not in glycopeptide_list:
            glycopeptide_list.append(df["Proteins"][i]+str(df["ProSites"][i])+df["Glycan(H,N,A,G,F,pH)"][i])
            glycan_size = 0
            for j in range(5):
                glycan_size += int(df["Glycan(H,N,A,G,F,pH)"][i].split(" ")[j])
            if glycan_size <= 5:
                glycan_size_dict[5] += 1
            elif 6 <= glycan_size <= 7:
                glycan_size_dict[6] += 1
            elif 8 <= glycan_size <= 9:
                glycan_size_dict[8] += 1
            elif 10 <= glycan_size <= 12:
                glycan_size_dict[10] += 1
            elif 13 <= glycan_size <= 15:
                glycan_size_dict[13] += 1
            else:
                glycan_size_dict[16] += 1

    print("here is the glycan size distribution:")
    print(glycan_size_dict)


# main
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

site_per_protein()
glycan_per_site()
glycan_size_distribution()
