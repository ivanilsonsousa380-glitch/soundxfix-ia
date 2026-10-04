name: Rodar VideoFacil Automatico

on:
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar codigo do repositorio
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Executar script videofacil
        run: python videofacil_cloud.py.
