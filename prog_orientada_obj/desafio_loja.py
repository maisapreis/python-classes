# !python
from datetime import datetime
from desafio_loja import Cliente, Vendedor, Compra # o arquivo __init__.py deixou estes expostos aqui.


def main():
    cliente = Cliente('Maisa Pierini Preis', 28)
    vendedor = Vendedor('Renan Bernhardt', 35, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 12, 25), 254)
    compra3 = Compra(cliente, datetime.now(), 845)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    cliente.registrar_compra(compra3)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_compras} compras')
    print(f'Ultima compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()