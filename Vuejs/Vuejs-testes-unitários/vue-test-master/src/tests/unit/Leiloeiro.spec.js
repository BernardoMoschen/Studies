import Leiloeiro from '@/views/Leiloeiro'
import { mount } from '@vue/test-utils'
import { getLeilao, getLances} from '@/http'
import flushPromises from 'flush-promises'

jest.mock('@/http')

const leilao = {
  produto: 'Livro da Casa do Código',
  lanceInicial: 50,
  descricao: 'Livro bem bacana sobre VueJS'
}

describe('Leiloeiro inicia leilão que não possui lances', () => {
  test('Avisa quando não existem lances', () => {

    getLeilao.mockResolvedValueOnce(leilao)
    getLances.mockResolvedValueOnce([])

    const wrapper = mount(Leiloeiro, {
      propsData: {
        id: 1,
      }
    })

    await flushPromises()

    const alerta = wrapper.find('.alert-dark')
    expect(alerta.exists()).toBeTruthy()
  })
})
