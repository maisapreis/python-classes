#! python

# Usando Programação Funcional - Callable e *args


def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens)) # Aqui tem um Generator, com ()
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':    
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco(inline=True, conteudo='inline')) # Aqui o parâmetro foi NOMEADO, para poder mudar a ordem.
    print(tag_bloco('falhou', classe='erro')) # Aqui o parâmetro foi NOMEADO.
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))

    print(tag_bloco(tag_lista('Sabado', 'Domingo'), classe='info', inline=True)) # Depois de *args (tupla) é obrigado usar parãmetros nomeados.




