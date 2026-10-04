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

      - name: Diagnostico Completo de Arquivos
        run: |
          echo "=== DIRETORIO ATUAL ==="
          pwd
          echo "=== LISTAGEM COMPLETA DE ARQUIVOS (TREE) ==="
          find . -maxdepth 3 -not -path '*/.*'
          echo "=== PROCURANDO PELO SCRIPT ==="
          find . -name "videofacil_cloud.py"

      - name: Executar script videofacil encontrado
        run: |
          ARQUIVO=$(find . -name "videofacil_cloud.py" | head -n 1)
          if [ -f "$ARQUIVO" ]; then
            echo "Executando: python $ARQUIVO"
            python "$ARQUIVO"
          else
            echo "ERRO CRITICO: Arquivo videofacil_cloud.py nao foi encontrado em nenhuma pasta!"
            exit 1
          fi
