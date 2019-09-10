def main ():
  import time,sys,os
  from Bio import Entrez, SeqIO
  from Bio.Blast import NCBIWWW
  print("\n")
  print("Starting to get PSI-BLAST results/other sequences in the " + sys.argv[1] + " protein family")
  
  start = time.time()   
  for numHits in ["20000"]:
    print("\n")
    print("Getting " + numHits + " PSI-BLAST results/sequences for the " + sys.argv[1] + " protein family")
    relative_name = "1_" + sys.argv[1] +"_Ref_Seq.fasta"
    absolute_name = "/home/" + sys.argv[2] + "/outputFiles/" + relative_name
    fasta_string = open(absolute_name).read()
    print("fetching from psi-blast")
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string, service = "psi", hitlist_size=int(numHits))
    print("done fetching from psi-blast")
    blast_result = open("2_"+ sys.argv[1] +"_" + numHits + "_BLAST.xml", "w")
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()
    print("\n")
    print("Done getting " + numHits + " PSI-BLAST results/sequences for the " + sys.argv[1] + " protein family")
  end = time.time()
  print("\n")
  print("This took " + str(end-start) + " seconds to complete")
main()
