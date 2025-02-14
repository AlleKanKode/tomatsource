# Episodenoter til TomatSource episode 12 om pypi pakker

Episode Number: 12

## Link til Youtube 
Se episoden her : https://youtube.com/live/udYl3ytdE-E

## Links omtalt i episoden

- [Cython en compiler pakke til c som bruger ‘setup.py](https://pypi.org/project/Cython/#files)’
- [Dokumentationen på PyPi omkring skift fra ‘setup.py’ til pyproject.toml](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)
- [Sikkerhedshjemmeside (deps.dev), der viser om en package (dependency) fra pypi kan være kompromiteret med malware](https://deps.dev/)
- [Meta Opensource Docusaurus til dokumentation af kode](https://docusaurus.io/)
- [Sphinx doc (som bruges af ‘pypi.org’ selv)](https://www.sphinx-doc.org/en/master/index.html)
- [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/)
- [Hvordan vælger du en Licens til din pakke?](https://choosealicense.com/)

Jeg fik ikke vist det i episoden, men hvis vi skal installere pakken fra episode 11 så kan man gøre det med denne uv kommando

```bash

uv add --index https://test.pypi.org/simple/ --index https://pypi.org/simple/ --index-strategy unsafe-best-match tomatsource11
```

Den skal jeg vise i en senere episode.

## Er du på maillisten, så får du også adgang til mine noter

Se mere på https://allekankode.dk