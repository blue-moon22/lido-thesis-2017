run_bowtie <- function(sample, folder_work) {
  # screen -r HMP_HUMAN_FILTER boogy5
  # Version: Bowtie2-2.2.3
  
  bowtie2 <- "/users/k1639482/brc_scratch/SOFTWARE/bowtie2-2.2.3/bowtie2"
  max_processors <- 40
  reference_human <- "/users/k1639482/brc_scratch/NECESSARY_FILES/bowtie2/homo_sapiens.fna"
  samples_REF <- c("homo_sapiens.fna.1.bt2", "homo_sapiens.fna.2.bt2", "homo_sapiens.fna.3.bt2", 
                   "homo_sapiens.fna.4.bt2", "homo_sapiens.fna.rev.1.bt2", "homo_sapiens.fna.rev.2.bt2")
  parameters_BT <- paste(" -q -N 1 -p  ",max_processors,"  -k 1 --fr -x ",reference_human,
                         " --end-to-end --phred33 --very-sensitive --no-discordant ",sep="")
  
  order <- c(bowtie2)
  order <- paste(order, " ", parameters_BT,
                 " -1 ",folder_work,"/",sample,"_trimmo_trimmed_1.fastq ",
                 " -2 ",folder_work,"/",sample,"_trimmo_trimmed_2.fastq ",
                 " -S /dev/null", # ",folder_work,"/",sample,"_trimmo_trimmed_human",".sam ",
                 " --un-conc ",folder_work,"/",sample,"_trimmo_trimmed_and_filtered","_%.fastq",sep="")
  print("Running bowtie2....")
  system(order)
}