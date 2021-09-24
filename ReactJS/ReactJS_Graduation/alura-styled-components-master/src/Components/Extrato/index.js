import React from 'react'
import { Box, GenericButton } from '../UI'
import { extratoLista } from '../../info'
import Items from '../Items'

const Extrato = () => {
  return (
    <Box>
      {extratoLista.updates.map(({id, type, from, value, date}) => {
        return (
          <Items key={id} type={type} from={from} value={value} date={date}/>
        )
      })}
      <GenericButton>Ver Mais</GenericButton>
    </Box>
  )
}

export default Extrato