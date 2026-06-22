# PNBench-ddG

This repository contains the datasets and scripts used to construct the
PNBench-ddG dataset.

- `dataset and results/`

  This folder contains all dataset files, curation records and similarity
  analysis results.

- `dataset and results/PNBench ddG/`

  This folder contains the final integrated PNBench-ddG dataset and the final
  cross-database curation files.

  - `PNBench_ddG.xlsx`: the final PNBench-ddG dataset. It contains the
    `protein-DNA` and `protein-RNA` sheets.
  - `merge_dataset_protein_DNA.xlsx`: the merged protein-DNA dataset. The
    workbook contains intermediate processing sheets and the final curated
    protein-DNA subset.
  - `merge_dataset_protein_RNA.xlsx`: the merged protein-RNA dataset. The
    workbook contains intermediate processing sheets and the final curated
    protein-RNA subset.
  - `mutation_delete_protein_DNA.xlsx`: records removed during final curation
    of the protein-DNA subset.
  - `mutation_delete_protein_RNA.xlsx`: records removed during final curation
    of the protein-RNA subset.

- `dataset and results/ProNAB/`

  This folder contains the original ProNAB data and the curated ProNAB
  protein-DNA/protein-RNA subsets.

  - `source_ProNAB.xlsx`: the original ProNAB dataset and source-level
    processing records.
  - `ProNAB_protein_DNA_mutation.xlsx`: the protein-DNA subset extracted from
    ProNAB. The workbook contains processing records and the curated DNA
    subset.
  - `ProNAB_protein_RNA_mutation.xlsx`: the protein-RNA subset extracted from
    ProNAB. The workbook contains processing records and the curated RNA
    subset.
  - `mutation_delete_source.xlsx`: records removed from the original ProNAB
    dataset before DNA/RNA subset curation.
  - `mutation_delete_protein_DNA.xlsx`: ProNAB protein-DNA records removed
    during curation.
  - `mutation_delete_protein_RNA.xlsx`: ProNAB protein-RNA records removed
    during curation.

- `dataset and results/ProNIT/`

  This folder contains the original ProNIT data and the curated ProNIT
  protein-DNA/protein-RNA subsets.

  - `source_ProNIT.xlsx`: the original ProNIT dataset and source-level
    processing records.
  - `ProNIT_protein_DNA_mutation.xlsx`: the protein-DNA subset extracted from
    ProNIT.
  - `ProNIT_protein_RNA_mutation.xlsx`: the protein-RNA subset extracted from
    ProNIT.

- `dataset and results/dbAMEPNI/`

  This folder contains the original dbAMEPNI data and the curated dbAMEPNI
  protein-DNA/protein-RNA subsets.

  - `source_dbAMEPNI.xlsx`: the original dbAMEPNI dataset.
  - `dbAMEPNI_protein_DNA_mutation.xlsx`: the protein-DNA subset extracted
    from dbAMEPNI.
  - `dbAMEPNI_protein_RNA_mutation.xlsx`: the protein-RNA subset extracted
    from dbAMEPNI.
  - `mutations_delete.xlsx`: dbAMEPNI records removed during curation.

- `dataset and results/Nabe/`

  This folder contains the original Nabe data and the curated Nabe
  protein-DNA/protein-RNA subsets.

  - `source_Nabe.xlsx`: the original Nabe dataset.
  - `Nabe_protein_DNA_mutations.xlsx`: the protein-DNA subset extracted from
    Nabe. The workbook contains deletion records and the final curated DNA
    subset.
  - `Nabe_protein_RNA_mutations.xlsx`: the protein-RNA subset extracted from
    Nabe. The workbook contains deletion records and the final curated RNA
    subset.

- `dataset and results/sequence_similarity_protein_DNA.xlsx`

  Pairwise protein sequence similarity results for the final protein-DNA
  subset.

- `dataset and results/sequence_similarity_protein_RNA.xlsx`

  Pairwise protein sequence similarity results for the final protein-RNA
  subset.

- `dataset and results/structure_similarity_protein_DNA.xlsx`

  Foldseek structural similarity results for the final protein-DNA subset.

- `dataset and results/structure_similarity_protein_RNA.xlsx`

  Foldseek structural similarity results for the final protein-RNA subset.

- `script/`

  This folder contains helper scripts used during repeated-measurement
  processing.

  - `count_repeat_mutations.py`: counts repeated mutation labels.
  - `calculating_std.py`: calculates standard deviation for repeated mutation
    labels.
  - `calculating_mean.py`: calculates mean values for repeated mutation
    labels.
