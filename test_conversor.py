import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROGRAMA = Path(__file__).with_name("conversor.py")


class TestConversorCSVJSON(unittest.TestCase):

    def executar(self, csv_texto, saida_inicial=None):
        with tempfile.TemporaryDirectory() as temp:
            pasta = Path(temp)
            entrada = pasta / "entrada.csv"
            saida = pasta / "saida.json"

            entrada.write_text(csv_texto, encoding="utf-8")

            if saida_inicial is not None:
                saida.write_text(saida_inicial, encoding="utf-8")

            resultado = subprocess.run(
                [
                    sys.executable,
                    str(PROGRAMA),
                    str(entrada),
                    str(saida),
                ],
                capture_output=True,
                text=True,
            )

            conteudo = (
                saida.read_text(encoding="utf-8")
                if saida.exists()
                else None
            )

            return resultado, conteudo

    def test_conversao_valida(self):
        resultado, conteudo = self.executar(
            "nome,idade,cidade\nAna,28,Itaperuna\n"
        )
        self.assertEqual(resultado.returncode, 0)
        dados = json.loads(conteudo)
        self.assertEqual(dados[0]["nome"], "Ana")
        self.assertEqual(dados[0]["idade"], 28)

    def test_campos_ausentes(self):
        marcador = "ARQUIVO ANTERIOR"
        resultado, conteudo = self.executar(
            "nome,idade,cidade\nAna,28\n", marcador
        )
        self.assertNotEqual(resultado.returncode, 0)
        self.assertEqual(conteudo, marcador)

    def test_campos_extras(self):
        resultado, _ = self.executar(
            "nome,idade\nAna,28,Itaperuna\n"
        )
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("valores extras", resultado.stdout)

    def test_idade_invalida(self):
        resultado, _ = self.executar(
            "nome,idade\nAna,vinte\n"
        )
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("idade inválida", resultado.stdout)

    def test_cabecalho_vazio(self):
        resultado, _ = self.executar("")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("CSV está vazio", resultado.stdout)

    def test_colunas_repetidas(self):
        resultado, _ = self.executar(
            "nome,idade,idade\nAna,28,30\n"
        )
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn("colunas repetidos", resultado.stdout)

    def test_arquivo_saida_preservado(self):
        marcador = "CONTEUDO ORIGINAL"
        resultado, conteudo = self.executar(
            "nome,idade\nAna,erro\n", marcador
        )
        self.assertNotEqual(resultado.returncode, 0)
        self.assertEqual(conteudo, marcador)


if __name__ == "__main__":
    unittest.main(verbosity=2)
