import re

# Ecolha o tamaho máximo
tamanho_maximo = 100


def reformatar_ofx(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.ofx', 'rb') as ofx:
        ofx_str = ofx.read().decode('latin-1')
        lista_names = re.findall(r'  m', ofx_str)

        for name in lista_names:

            name_limpo = name.replace('<NAME>', "").replace('</NAME>', '')
            if len(name_limpo) >= tamanho_maximo:
                name_limpo = name_limpo[:tamanho_maximo - 1]
                print(name, "---->", f'<NAME>{name_limpo}</NAME>')
                name_final = f'<NAME>{name_limpo}</NAME>'
                ofx_str = ofx_str.replace(name, name_final)
    with open('ofx_reformatado.ofx', 'wb') as ofx:
        try:
            ofx.write(ofx_str.encode('latin-1'))
        except:
            raise ValueError('Não existem erros para serem corrigidos')
    return 'ofx_reformatado.ofx'

