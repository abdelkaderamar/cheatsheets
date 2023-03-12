#! /bin/bash -u

build() {
  for md_file in "$@"
  do
    echo "[colourful] generating $md_file"
    python md_to_latex_colourful.py "$md_file"
    echo "[colourful-updated] generating $md_file"
    python md_to_latex_colourful.py -u "$md_file"
    echo "[basic_template] generating $md_file"
    python md_to_latex.py "$md_file"
  done

  # TODO: fix (md vs yaml)
  # for yaml_file in */*.yaml
  # do
  #  python yaml_to_latex.py "$yaml_file"
  # done
}

if [ $# -eq 0 ]
then
  build */*.md
else
  build "$@"
fi

