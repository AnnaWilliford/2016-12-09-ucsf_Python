## File Key
- generate_all_data.sh = script used to download, analyze, and generate the full dataset we're working with
  * Note that "." fields in final file represent windows where no elements mapped. I changed them to 'NA' for our exercise, but they should really be '0'.
- human_chr21.txt = text file of human chr21 data, without issues
- human_chr21.xlsx = Excel file of human chr21 data, without issues
- human_chr21_broken.xlsx = Excel file of human chr21 data, but with issues that need to be corrected
  * cell with issue (row(s):column(s) - 0 indexed
  * 0:1-2 - both headers are 'window', but should be 'window_start' and 'window_end'
  * 2:5-7 - various encodings of missing data, standardize to 'NA
  * 9:3 - 0 (the number) encoded as O (the letter)
  * 15:0 - should be 'chr1' instead of 'chr_1'
  * 2,14:8 - spurious commment that should be deleted
  * 22:3 - spurious comment that should be deleted
- human_window_stats.zip = window stats for each chr as separate files, without issues
- human_window_stats_sab.zip = window stats for each chr as separate files, with issues that need correcting
- vertebrate_window_stats.zip = window stats for each chr as separate files for 4 vertebrate species, without issues
  * `human chr4.txt` should be `human_chr4.txt` for consistency
  * `human.chr16.txt` should be `human_chr16.txt` for consistency
  * `human_chr1.txt` contains data for chr1, chr10, and chr11 (but not in order). Demonstrates a common wild-card issue that people encounter. Need to use `sort` and `head`/`tail` to separate out. `human_chr10.txt` and `human_chr11.txt` files are fine, so can overwrite them or just delete proper lines in `human_chr1.txt`
  * `human_chrSex.txt` contains information about the `X` and `Y` chromosomes, but pasted side by side. Need to use `cut` to extract each into `human_chrX.txt` and `human_chrY.txt`, and delete the original.
