import React from 'react'
import App, {calcularNovoSaldo} from './App'
import {render, screen} from '@testing-library/react'

describe('Componente principal', () => {
    describe('Quando eu abro o App,', () => {
        it('O nome do banco e exibido', () => {
            render(<App/>);
            expect(screen.getByText('ByteBank')).toBeInTheDocument()
        })
    
        it('Meu saldo e exibido', () => {
            render(<App/>);
            expect(screen.getByText('Saldo:')).toBeInTheDocument()
        })
    
        it('O botao de realizar transacao e exibido', () => {
            render(<App/>);
            expect(screen.getByText('Realizar operação')).toBeInTheDocument()
        }) 
    })

    describe('Quando eu realizado uma transacao,', () => {
        it('de saque, o valor diminui', () => {
            const valores = {
                transacao: 'saque',
                valor: 50
            }
            const novoSaldo = calcularNovoSaldo(valores, 150);
            expect(novoSaldo).toBe(100)
        })
    })
})
