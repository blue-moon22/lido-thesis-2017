alientrimmer <- function(sample, folder_work) {
  # ADAPTERS INFORMATION
  # http://bioinformatics.cvr.ac.uk/blog/illumina-adapter-and-primer-sequences/
  # http://support.illumina.com/downloads/illumina-customer-sequence-letter.html
  # http://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/experiment-design/illumina-adapter-sequences_1000000002694-01.pdf
  
  alientrimmer <- "/users/k1639482/brc_scratch/SOFTWARE/AlienTrimmer_0.4.0/src/AlienTrimmer.jar"
  parameters_AT <- " -k 10 -l 45 -m 5 -p 40 -q 20 "
  # Only p changed from default 0
  
  set_primers <- "/users/k1639482/brc_scratch/NECESSARY_FILES/alienTrimmerPF8contaminants.fasta"
  
  order <- c("java -jar -d64 -Xmx512M")
  order <- paste(order, " " ,alientrimmer," ", parameters_AT,
                 " -if ",folder_work,"/",sample,"_1.fastq ",
                 " -ir ",folder_work,"/",sample,"_2.fastq ",
                 " -c ",set_primers," ",
                 " -of ",folder_work,"/",sample,"_trimmo_trimmed_1.fastq",
                 " -or ",folder_work,"/",sample,"_trimmo_trimmed_2.fastq",
                 " -os ",folder_work,"/",sample,"_trimmo_trimmed_s.fastq",
                 sep="")
  system(order)
}