
TOTAL_PESSOAS = 2

alturas = []
generos = []

print("=" * 50)
print(f"CADASTRO DE {TOTAL_PESSOAS} PESSOAS")
print("=" * 50)

for i in range(1, TOTAL_PESSOAS + 1):
    print(f"\n--- Pessoa {i} ---")

    # Validação da altura
    while True:
        try:
            altura = float(input("Altura (em metros, ex: 1.75): "))
            if altura <= 0:
                print("A altura deve ser um valor positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número (ex: 1.75).")

    # Validação do gênero
    while True:
        genero = input("Gênero (M - Masculino / F - Feminino): ").strip().upper()
        if genero in ("M", "F"):
            break
        print("Opção inválida. Digite apenas 'M' ou 'F'.")

    alturas.append(altura)
    generos.append(genero)

# ---------- CÁLCULOS ----------

maior_altura = max(alturas)
menor_altura = min(alturas)

alturas_masculino = [alturas[i] for i in range(TOTAL_PESSOAS) if generos[i] == "M"]
media_masculino = sum(alturas_masculino) / len(alturas_masculino) if alturas_masculino else 0

qtd_feminino = generos.count("F")

# ---------- RESULTADOS ----------

print("\n" + "=" * 50)
print("RESULTADOS")
print("=" * 50)
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")

if alturas_masculino:
    print(f"Média de altura (Masculino): {media_masculino:.2f} m")
else:
    print("Não há pessoas do gênero Masculino cadastradas.")

print(f"Número de pessoas do gênero Feminino: {qtd_feminino}")