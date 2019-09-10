def main():
  import pandas as pd
  import sys
  print("\n")
  print("Transposing files...")
  for file in ["2_" + sys.argv[1] + "_20000_BLAST.csv"]:
    pd.read_csv(file).T.to_csv(file,header=False)
  print("\n")
  print("Done transposing files...")
main()
