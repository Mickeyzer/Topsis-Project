import sys
import os
import pandas as pd
import numpy as np

def error_exit(msg: str,code: int =1):
    print(f"Error: {msg}")
    raise SystemExit(code)

def parse_csv_list(s: str,kind:str):
    if "," not in s:
        error_exit(f'{kind} must be seperated by "," ')

    parts=[p.strip() for p in s.split(",")]
    if any(p=="" for p in parts):
        error_exit(f'{kind} contains empty value(s)')
    return parts

def read_input_file(filename:str) -> pd.DataFrame:
    if not os.path.isfile(filename):
        error_exit(f'File not found: "{filename}"')
    if not filename.lower().endswith(".csv"):
        error_exit(f'Unsupported file format')

    try:
        return pd.read_csv(filename)
    except Exception as e:
        error_exit(f'Error reading input file: {e}')

def topsis(df: pd.DataFrame, weights: np.ndarray, impacts: np.ndarray):
    X=df.to_numpy(dtype=float)

    R=X/np.sqrt((X**2).sum(axis=0))
    V=R*weights
    
    best = np.zeros(V.shape[1])
    worst = np.zeros(V.shape[1])

    for j in range(V.shape[1]):
        if impacts[j]=="1":
            best[j]=V[:,j].max()
            worst[j]=V[:,j].min()
        else:
            best[j]=V[:,j].min()
            worst[j]=V[:,j].max()
    
    dpos=np.sqrt(((V-best)**2).sum(axis=1))
    dneg=np.sqrt(((V-worst)**2).sum(axis=1))

    score=dneg/(dpos+dneg)
    rank=(-score).argsort().argsort() +1

    return score, rank

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    if len(argv) !=5:
        print("Usage:")
        print("  topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        raise SystemExit(1)
    
    input_file,weights_str,impacts_str,output_file=argv[1:]
    data=read_input_file(input_file)

    if data.shape[1]<3:
        error_exit("Input file must contain at least three columns")

    criteria_cols=data.columns[1:]
    criteria=data[criteria_cols].copy()

    for col in criteria_cols:
        criteria[col]=pd.to_numeric(criteria[col],errors="coerce")

    if criteria.isnull().values.any():
        error_exit("Non-numeric data found in criteria columns")

    weights_list=parse_csv_list(weights_str,"Weights")
    impacts_list=parse_csv_list(impacts_str,"Impacts")

    if len(weights_list) != len(criteria_cols):
        error_exit("Number of weights must match number of criteria columns.")

    if len(impacts_list) != len(criteria_cols):
        error_exit("Number of impacts must match number of criteria columns.")

    try:
        weights = np.array(weights_list, dtype=float)
    except ValueError:
        error_exit("Weights must be numeric.")

    if np.any(weights < 0):
        error_exit("Weights must be non-negative.")

    impacts = []
    for i in impacts_list:
        if i not in ["+", "-"]:
            error_exit('Impacts must be "+" or "-".')
        impacts.append(1 if i == "+" else -1)
    impacts = np.array(impacts)

    scores, ranks = topsis(criteria, weights, impacts)

    result = data.copy()
    result["Topsis Score"] = scores
    result["Rank"] = ranks

    try:
        result.to_csv(output_file, index=False)
    except Exception as e:
        error_exit(f"Could not write output file: {e}")

    print(f"TOPSIS result saved to '{output_file}'")


if __name__ == "__main__":
    main()