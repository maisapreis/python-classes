#! python

# Usando **kwargs

# Criar tuplas para filtrar.
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados): 
    return ' '.join(f'{k.split("_")[-1]}="{v}"' # key="value" do HTML.
        for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens)) # Aqui tem um Generator, com ()
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)} {lista}</ul>'


if __name__ == '__main__':    
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco(inline=True, conteudo='inline')) # Aqui o parâmetro foi NOMEADO, para poder mudar a ordem.
    print(tag_bloco('falhou', classe='erro')) # Aqui o parâmetro foi NOMEADO.
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista('Sabado', 'Domingo'), classe='info', inline=True)) # Depois de *args (tupla) é obrigado usar parãmetros nomeados.


    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', ul_style='color:red'))

