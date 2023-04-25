import json
import requests

with open('./files/base_tdspy.json') as file:
    jsonFile = json.load(file)

def remove_com(enumerated_url):
    index, url = enumerated_url
    url_sem_com = url.split(".")[0]
    return f"{index + 1} - {url_sem_com.capitalize()}"

# code
#   - variables
isValid = False
insertRm = None
optionSelect = None

#   - get RM
while not isValid:
    insertRm = input('\nDigite os números do seu RM (Ex.:123456): ')

    if insertRm in jsonFile:
        isValid = True
    else:
        print("\nPor favor, digite um RM valido.\n")

number_loop = 1
while number_loop == 1:

    #   - getting options and turning options into string
    isValid = False
    urls = jsonFile[insertRm]
    resultArray = list(map(remove_com, enumerate(urls)))
    result_string = "\n".join(resultArray)

    #   - getting selected option
    while not isValid:
        print("\nEssas são suas opções:")
        print(result_string)
        optionSelect = int(input("Escolha uma delas usando o número na frente delas: ")) - 1

        if optionSelect >= 0 and optionSelect <= len(urls):
            isValid = True
        else:
            print("\nPor favor, escolha uma opção válida.")

    #   - getting site
    print("\nPegando seus dados na nuvem...")
    response = requests.get(f"https://www.{urls[optionSelect]}")
    print("Ok, tudo certo, dados pegos com sucesso!\nSalvando os dados...")
    file_html = response.content


    #   - saving file
    name_html = urls[optionSelect].split(".")[0]
    with open('./files/' + name_html + '.html', 'w') as file_site:
        file_site.write(str(file_html))
    print("Dados salvos!\n")
    number_loop = int(input("Digite 1 para salvar outra HTML\nDigite 2 para sair do programa: "))


