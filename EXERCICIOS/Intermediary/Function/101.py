def voto(num):
    idade=2026-num
    if idade>=18:
        return f'Com {idade}: Obrigatório!'
    elif idade<=15:
        return f'Com {idade}: Não vota!'
    elif idade>=65: f'Com {idade}: Opcional!'
    else:
        return f'Com {idade}: Opcional!'
print(voto(2008))




