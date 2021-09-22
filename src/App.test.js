import React from 'react'
import App from './App'
import {render, screen} from '@testing-library/react'

describe('Main component', () => {
    it('Mostra o nome do banco', () => {
        render(<App/>);
        expect(screen.getByText('ByteBank')).toBeInTheDocument()
    })
})
