import React from 'react'
import App from './App'
import {render, screen} from '@testing-library/react'

describe('Main component', () => {
    describe('When i open the app,', () => {
        it('the bank name is displayed', () => {
            render(<App/>);
            expect(screen.getByText('ByteBank')).toBeInTheDocument()
        })
    
        it('my balance is displayed', () => {
            render(<App/>);
            expect(screen.getByText('Saldo:')).toBeInTheDocument()
        })
    
        it('the perform transaction button is displayed', () => {
            render(<App/>);
            expect(screen.getByText('Realizar operação')).toBeInTheDocument()
        }) 
    })
})
