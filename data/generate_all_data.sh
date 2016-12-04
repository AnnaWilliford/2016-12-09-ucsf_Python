#!/usr/bin/env zsh

# download full genomes
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.35_GRCh38.p9/GCF_000001405.35_GRCh38.p9_genomic.fna.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Gallus_gallus/latest_assembly_versions/GCF_000002315.4_Gallus_gallus-5.0/GCF_000002315.4_Gallus_gallus-5.0_genomic.fna.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Anolis_carolinensis/latest_assembly_versions/GCF_000090745.1_AnoCar2.0/GCF_000090745.1_AnoCar2.0_genomic.fna.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Xenopus_laevis/latest_assembly_versions/GCF_001663975.1_Xenopus_laevis_v2/GCF_001663975.1_Xenopus_laevis_v2_genomic.fna.gz

# download annotation GFFs
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.35_GRCh38.p9/GCF_000001405.35_GRCh38.p9_genomic.gff.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Gallus_gallus/latest_assembly_versions/GCF_000002315.4_Gallus_gallus-5.0/GCF_000002315.4_Gallus_gallus-5.0_genomic.gff.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Anolis_carolinensis/latest_assembly_versions/GCF_000090745.1_AnoCar2.0/GCF_000090745.1_AnoCar2.0_genomic.gff.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Xenopus_laevis/latest_assembly_versions/GCF_001663975.1_Xenopus_laevis_v2/GCF_001663975.1_Xenopus_laevis_v2_genomic.gff.gz

# download repeat annotations
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.35_GRCh38.p9/GCF_000001405.35_GRCh38.p9_rm.out.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Gallus_gallus/latest_assembly_versions/GCF_000002315.4_Gallus_gallus-5.0/GCF_000002315.4_Gallus_gallus-5.0_rm.out.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Anolis_carolinensis/latest_assembly_versions/GCF_000090745.1_AnoCar2.0/GCF_000090745.1_AnoCar2.0_rm.out.gz
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_other/Xenopus_laevis/latest_assembly_versions/GCF_001663975.1_Xenopus_laevis_v2/GCF_001663975.1_Xenopus_laevis_v2_rm.out.gz

# must do following steps manually, since chromosome names differ drastically
# subset genomes to placed chromosomes and give nice names (i.e., chr...)
echo "creating nice genome files with nice chromosome names"
seqtk seq GCF_000001405.35_GRCh38.p9_genomic.fna.gz | grep -A1 --no-group-separator "NC_0000[0-9][0-9]" | sed 's/NC_0000[0-9][0-9].[0-9][0-9] Homo sapiens chromosome /chr/g' | sed 's/NC_0000[0-9][0-9].[0-9] Homo sapiens chromosome /chr/g' | sed 's/, GRCh38.p7 Primary Assembly//g' | gzip > GCF_000001405.35_GRCh38.p9_genomic_reformat.fna.gz
seqtk seq GCF_000002315.4_Gallus_gallus-5.0_genomic.fna.gz | grep -A1 --no-group-separator "NC_006" | sed 's/NC_006[0-9][0-9][0-9].[0-9] Gallus gallus isolate RJF #256 breed Red Jungle fowl, inbred line UCD001 chromosome /chr/g' | sed 's/, Gallus_gallus-5.0, whole genome shotgun sequence$//g' | gzip > GCF_000002315.4_Gallus_gallus-5.0_genomic_reformat.fna.gz
seqtk seq GCF_000090745.1_AnoCar2.0_genomic.fna.gz | grep -A1 "NC_0147" | sed 's/NC_0147[0-9][0-9].[0-9] Anolis carolinensis chromosome /chr/g' | sed 's/NC_0147[0-9][0-9].[0-9] Anolis carolinensis linkage group /chr_lg/g' | sed 's/, AnoCar2.0, whole genome shotgun sequence//g' | gzip > GCF_000090745.1_AnoCar2.0_genomic_reformat.fna.gz
seqtk seq GCF_001663975.1_Xenopus_laevis_v2_genomic.fna.gz | grep -A1 "NC_0307" | sed 's/NC_0307[0-9][0-9].1 Xenopus laevis strain J chromosome /chr/g' | sed 's/, Xenopus_laevis_v2, whole genome shotgun sequence//g' | gzip > GCF_001663975.1_Xenopus_laevis_v2_genomic_reformat.fna.gz

# create association between old and new chromsome names
# creating an association file between old chromsome names and new ones
paste <(seqtk seq GCF_000001405.35_GRCh38.p9_genomic.fna.gz | grep --no-group-separator "NC_0000[0-9][0-9]" | cut -d " " -f 1 | sed 's/>//g') <(zcat GCF_000001405.35_GRCh38.p9_genomic_reformat.fna.gz | grep ">" | sed 's/>//g') > GCF_000001405.35_GRCh38.p9_chr_association.tsv
paste <(seqtk seq GCF_000002315.4_Gallus_gallus-5.0_genomic.fna.gz | grep --no-group-separator "NC_006" | cut -d " " -f 1 | sed 's/>//g') <(zcat GCF_000002315.4_Gallus_gallus-5.0_genomic_reformat.fna.gz | grep ">" | sed 's/>//g') > GCF_000002315.4_Gallus_gallus-5.0_chr_association.tsv
paste <(seqtk seq GCF_000090745.1_AnoCar2.0_genomic.fna.gz | grep --no-group-separator "NC_0147" | cut -d " " -f 1 | sed 's/>//g') <(zcat GCF_000090745.1_AnoCar2.0_genomic_reformat.fna.gz | grep ">" | sed 's/>//g') > GCF_000090745.1_AnoCar2.0_chr_association.tsv
paste <(seqtk seq GCF_001663975.1_Xenopus_laevis_v2_genomic.fna.gz | grep "NC_0307" | cut -d " " -f 1 | sed 's/>//g') <(zcat GCF_001663975.1_Xenopus_laevis_v2_genomic_reformat.fna.gz | grep ">" | sed 's/>//g') > GCF_001663975.1_Xenopus_laevis_v2_chr_association.tsv

# now that we have nicely-formated files, we can automate the rest using a while loop
# must first create prefixes for each genome for the loop
echo "setting up environment for processing loop"
echo -e "GCF_000001405.35_GRCh38.p9\thuman\nGCF_000002315.4_Gallus_gallus-5.0\tchicken\nGCF_000090745.1_AnoCar2.0\tlizard\nGCF_001663975.1_Xenopus_laevis_v2\tfrog" > genomes.txt

# and create output directories for each genome
mkdir human
mkdir chicken
mkdir lizard
mkdir frog

# then can run each through a series of commands to generate the data we want:
# 1. index genome using samtools faidx
# 2. make 1Mb windows using bedtools
# 3. create BED of exon coordinates with nice chromosome names
# 4. use BED of exons and windows to calculate number of coding bp per window
# 5. create BED of simple repeat coordinates with nice chromosome names
# 6. create BED of complex repeat coordinates with nice chromosome names
# 7. use BED of simple repeats and windows to calcualte number of simple repeat bp per window
# 8. use BED of complex repeats and windows to calcualte number of complex repeat bp per window
# 9. determine number of ambiguous and G/C bp per window
# 10. merge all BED stat outputs into one final stats file
# 11. split final stats file by chromosome
echo "running data processing loop"
cat genomes.txt | while IFS="$(printf '\t')" read -r genome species; do
echo $species;
echo "1";
samtools faidx "$genome"_genomic_reformat.fna.gz;
echo "2";
bedtools makewindows -n 20 -g "$genome"_genomic_reformat.fna.gz.fai | sortBed -i - > "$genome"_windows.bed;
echo "3";
cat "$genome"_chr_association.tsv | while IFS="$(printf '\t')" read -r f1 f2; do cmd="zcat "$genome"_genomic.gff.gz | grep "$f1" | sed 's/^$f1/$f2/g'"; eval $cmd; done | awk '{ if ($3 ~ "exon") print $0 }' | awk -v OFS="\t" '{ print $1,$4,$5,"exon",$5-$4,"+" }' | sortBed -i - > "$genome"_genomic_reformat_exons.bed;
echo "4";
bedtools map -a "$genome"_windows.bed -b "$genome"_genomic_reformat_exons.bed -c 5 -o sum > "$genome"_coding.bed;
echo "5";
cat "$genome"_chr_association.tsv | while IFS="$(printf '\t')" read -r f1 f2; do cmd="zcat "$genome"_rm.out.gz | grep "$f1" | sed 's/$f1/$f2/g'"; eval $cmd; done | awk '{ if ($11 ~ "Simple" || $11 ~ "Satellite" || $11 ~ "Low_complexity") print $0 }' | awk -v OFS="\t" '{ print $5,$6,$7,$11,$7-$6,"+" }' | sortBed -i - > "$genome"_rm_simple.bed;
echo "6";
cat "$genome"_chr_association.tsv | while IFS="$(printf '\t')" read -r f1 f2; do cmd="zcat "$genome"_rm.out.gz | grep "$f1" | sed 's/$f1/$f2/g'"; eval $cmd; done | awk '{ if ($11 !~ "Simple" && $11 !~ "Satellite" && $11 !~ "Low_complexity") print $0 }' | awk -v OFS="\t" '{ print $5,$6,$7,$10,$7-$6,"+" }' | sortBed -i - > "$genome"_rm_complex.bed;
echo "7";
bedtools map -a "$genome"_windows.bed -b "$genome"_rm_simple.bed -c 5 -o sum > "$genome"_simple_repeats.bed;
echo "8";
bedtools map -a "$genome"_windows.bed -b "$genome"_rm_complex.bed -c 5 -o sum > "$genome"_complex_repeats.bed;
echo "9";
seqtk subseq "$genome"_genomic_reformat.fna.gz "$genome"_windows.bed | seqtk comp | awk -F ':|-|\t' -v OFS="\t" '{ if ($5+$6+$7+$8 != 0) print $1,$2-1,$3,$4-($5+$6+$7+$8),($6+$7); else print $1,$2-1,$3,$4-($5+$6+$7+$8),"0" }' | sortBed -i - > "$genome"_gc.bed;
echo "10";
paste "$genome"_gc.bed "$genome"_coding.bed "$genome"_simple_repeats.bed "$genome"_complex_repeats.bed | awk -v OFS="\t" '{ print $1,$2,$3,$4,$5,$9,$13,$17 }' > "$genome"_full_stats.tsv;
echo "11";
while read chromosome; do grep -w "$chromosome" "$genome"_full_stats.tsv > "$species"/"$species"_$chromosome.txt; done < <(cat "$genome"_full_stats.tsv | cut -f 1 | uniq);
done
