main_title: Linux Command Cheatsheet
lang: bash

#---------------------------------------------------
title: Interleave lines of two text files
paste -d '\n' file1 file2
#---------------------------------------------------
title: exiftool - Renaming images
# Renames all images in directory "DIR" according to the individual file's creation date in the form "YYYYmmdd\_HHMMSS.ext".
exiftool "-FileName<CreateDate"
     -d "%Y%m%d_%H%M%S.%%e" DIR
#---------------------------------------------------
title: List package content (before installing it)
apt-file update
apt list package_name
#---------------------------------------------------
title: List (installed) package content
dpkg -L package_name
#---------------------------------------------------
title: Which package provides a file
dpkg -S file_absolute_path
#---------------------------------------------------
title: Find which package provides a file (not installed)
apt-file search file
#---------------------------------------------------
title: exiftool - Moving images
Moves all images originally in directory "DIR" into a directory hierarchy organized by year/month/day
exiftool "-Directory<DateTimeOriginal" -d "%Y/%m/%d" DIR
#---------------------------------------------------
title: Mount a disk
udisksctl mount -b /dev/sdg1
#---------------------------------------------------
title: Rename images in directory ``DIR'' into a directory hierarchy organized by ``Model''/year-month-day/date\_time.extension and preserve file date
exiftool -o . '-FileName<${model}/${CreateDate}' -d '%Y-%m-%d/%Y%m%d_%H%M%S.%%e' . -P

#---------------------------------------------------
title: Change or remove Camera Model Name tag from an image
exiftool -'Model'= 20190607_213819.jpg
#---------------------------------------------------

