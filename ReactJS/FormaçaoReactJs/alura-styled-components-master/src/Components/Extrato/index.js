import React from 'react'
import { Box } from '../UI'
import { extratoLista } from '../../info'

const Extrato = () => {
  return (
    <Box>
      {extratoLista.updates.map(({id, type, from, value, date}) => {
        return (
          <div key={id}>
            <div>{type}</div>
            <div>{from}</div>
          </div>
        )
      })}
    </Box>
  )
}

export default Extrato
