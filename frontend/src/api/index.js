import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
})

export async function calculateAngel(name) {
  const { data } = await api.post('/calculate', { name })
  return data
}

export async function calculateChineseAngel({ gender, ownName, parent1Name, parent2Name, surname }) {
  const { data } = await api.post('/calculate-chinese', {
    gender, ownName, parent1Name, parent2Name, surname
  })
  return data
}
