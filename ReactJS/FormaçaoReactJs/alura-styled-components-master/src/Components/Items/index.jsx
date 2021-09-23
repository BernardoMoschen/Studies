import React from 'react'
import styled from 'styled-components'
import Item from '../Item/Item'
import ImageFilter from '../ImageFIlter'

const Items = styled.div`
box-shadow: 4px 4px 20px 0px rgba(0, 0, 0, 0.1);
border-radius: 10px;
margin: 2px:
align-items: center;
display: flex;
justify-content: space-around;
padding: 10px;
font-size: 10px
`

export default (props) => 
  <Items>
    {ImageFilter(props.type)}
    <Item {...props}/>
    <span>{props.date}</span>
  </Items>
