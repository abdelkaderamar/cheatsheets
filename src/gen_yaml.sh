#! /bin/bash -u

build() {
  for yaml_file in */*.yaml
   do
    python yaml_to_latex.py "$yaml_file"
   done
}

if [ $# -eq 0 ]
then
  build */*.md
else
  build "$@"
fi

