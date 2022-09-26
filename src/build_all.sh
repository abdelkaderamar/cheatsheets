#! /bin/bash -u

for md_file in */*.md
do
  python md_to_latex_colourful.py "$md_file"
  python md_to_latex_colourful.py -u "$md_file"
  python md_to_latex.py "$md_file"
done

for yaml_file in */*.yaml
do
  python yaml_to_latex.py "$yaml_file"
done
