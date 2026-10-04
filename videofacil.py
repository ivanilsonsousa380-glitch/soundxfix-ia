import os
import sys

print("=== INICIANDO O VIDEOFACIL CLOUD ===")

print(f"Diretório de trabalho atual: {os.getcwd()}")
print(f"Versão do Python: {sys.version}")

def main():
    print("Executando rotina principal de geração...")
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Pasta '{output_dir}' criada com sucesso.")
        
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
