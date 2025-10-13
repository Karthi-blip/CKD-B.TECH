import pandas as pd
import numpy as np
import random

# Number of rows
n = 100000

np.random.seed(42)
random.seed(42)

# Helper function to decide CKD probability
def assign_ckd(age, bp, rbc, bgr, sc):
    score = 0
    if age > 50:
        score += 1
    if bp > 120:
        score += 1
    if rbc == "abnormal":
        score += 1
    if bgr > 140:
        score += 1
    if sc > 1.5:
        score += 1
    # Higher score = higher chance of CKD
    return "ckd" if random.random() < score/6 else "notckd"

# Generate random data
age = np.random.randint(1, 100, n)
bp = np.random.randint(50, 180, n)
sg = np.round(np.random.uniform(1.01, 1.03, n), 2)
al = np.random.randint(0, 5, n)
su = np.random.randint(0, 5, n)
rbc = np.random.choice(["normal", "abnormal"], n)
pc = np.random.choice(["normal", "abnormal"], n)
pcc = np.random.choice(["present", "notpresent"], n)
ba = np.random.choice(["present", "notpresent"], n)
bgr = np.random.randint(70, 500, n)
bu = np.random.randint(5, 100, n)
sc = np.round(np.random.uniform(0.5, 5.0, n), 2)
sod = np.random.randint(100, 160, n)
pot = np.random.randint(3, 7, n)
hemo = np.round(np.random.uniform(5, 18, n), 1)
pcv = np.random.randint(20, 60, n)
wc = np.random.randint(3000, 10000, n)
rc = np.round(np.random.uniform(3.0, 6.0, n), 1)
htn = np.random.choice(["yes", "no"], n)
dm = np.random.choice(["yes", "no"], n)
cad = np.random.choice(["yes", "no"], n)
appet = np.random.choice(["good", "poor"], n)
pe = np.random.choice(["yes", "no"], n)
ane = np.random.choice(["yes", "no"], n)

# Assign classification based on realistic conditions
classification = [assign_ckd(age[i], bp[i], rbc[i], bgr[i], sc[i]) for i in range(n)]

# Build DataFrame
df = pd.DataFrame({
    "id": np.arange(n),
    "age": age,
    "bp": bp,
    "sg": sg,
    "al": al,
    "su": su,
    "rbc": rbc,
    "pc": pc,
    "pcc": pcc,
    "ba": ba,
    "bgr": bgr,
    "bu": bu,
    "sc": sc,
    "sod": sod,
    "pot": pot,
    "hemo": hemo,
    "pcv": pcv,
    "wc": wc,
    "rc": rc,
    "htn": htn,
    "dm": dm,
    "cad": cad,
    "appet": appet,
    "pe": pe,
    "ane": ane,
    "classification": classification
})

# Save CSV
df.to_csv("ckd_dataset_100k_realistic.csv", index=False)
print("Realistic CKD dataset with 100,000 rows created as ckd_dataset_100k_realistic.csv")
