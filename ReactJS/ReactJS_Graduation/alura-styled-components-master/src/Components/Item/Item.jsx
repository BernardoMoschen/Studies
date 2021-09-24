import React from 'react'
import styled from 'styled-components'

const Item = styled.div`
display: flex;
flex-direction: column;

.text {
  font-Weight: bold;
}
`

export default ({type, from, value}) => (
  <Item>
  <span className="text">
  {type}
  </span>
  <span>
  {from}
  </span>
  <span>
  {value}
  </span>
  </Item>
  )
