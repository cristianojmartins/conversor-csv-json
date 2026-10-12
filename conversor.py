import csv
import json
import sys
from pathlib import Path


def converter_csv_para_json(arquivo_csv, arquivo_json):
    caminho_csv = Path(arquivo_csv)
    caminho_json = Path(arquivo_json)

    if not caminho_csv.is_file():
        print(f"Erro: arquivo não encontrado: {caminho_csv}")
        return False

    try:
        with caminho_csv.open(
            "r", encoding="utf-8-sig", newline=""
        ) as entrada:
            leitor = csv.DictReader(entrada)

            if not leitor.fieldnames:
                print("Erro: o CSV está vazio ou sem cabeçalho.")
                return False

            if any(not coluna.strip() for coluna in leitor.fieldnames):
                print("Erro: existe uma coluna sem nome.")
                return False

            if len(set(leitor.fieldnames)) != len(leitor.fieldnames):
                print("Erro: existem nomes de colunas repetidos.")
                return False

            registros = []

            for numero_linha, linha in enumerate(leitor, start=2):
                if None in linha:
                    print(
                        f"Erro: linha {numero_linha} "
                        "tem valores extras."
                    )
                    return False

                if any(valor is None for valor in linha.values()):
                    print(
                        f"Erro: linha {numero_linha} "
                        "tem campos ausentes."
                    )
                    return False

                if "idade" in linha:
                    try:
                        linha["idade"] = int(linha["idade"])
                    except ValueError:
                        print(
                            f"Erro: idade inválida na linha "
                            f"{numero_linha}."
                        )
                        return False

                registros.append(linha)

        with caminho_json.open("w", encoding="utf-8") as saida:
            json.dump(
                registros,
                saida,
                ensure_ascii=False,
                indent=2
            )

        print(f"Conversão concluída: {caminho_json}")
        print(f"Registros convertidos: {len(registros)}")
        return True

    except (OSError, csv.Error, UnicodeError, ValueError) as erro:
        print(f"Erro durante a conversão: {erro}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python conversor.py entrada.csv saida.json")
        sys.exit(1)

    sucesso = converter_csv_para_json(sys.argv[1], sys.argv[2])
    sys.exit(0 if sucesso else 1)
