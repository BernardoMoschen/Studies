import Lance from '@/components/Lance'
import { mount } from '@vue/test-utils'


describe('Um lance sem valor minimo', () => {
  test('verifica se há wrapper', () =>{
    const wrapper = mount(Lance)
    expect(wrapper).toBeTruthy()
  })

  test('verifica se o input existe', () => {
    const wrapper = mount(Lance)
    const input = wrapper.find('input')
    expect(input).toBeTruthy()
  })

  test('não aceita lance com valor menor que zero', () => {
    const wrapper = mount(Lance)
    const input = wrapper.find('input')
    input.setValue(-100)
    wrapper.trigger('submit')
    const lancesEmitidos = wrapper.emitted('novo-lance')
    expect(lancesEmitidos).toBeUndefined()
  })

  