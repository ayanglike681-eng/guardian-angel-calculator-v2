const SOLAR_TEMPLATE = [
  [6,  32, 3,  34, 35, 1],
  [7,  11, 27, 28, 8,  30],
  [19, 14, 16, 15, 23, 24],
  [18, 20, 22, 21, 17, 13],
  [25, 29, 10, 9,  26, 12],
  [36, 5,  33, 4,  2,  31]
]

function calculateHandle(num) {
  let n = Math.abs(num)
  while (n > 9) {
    n = n.toString().split('').reduce((acc, d) => acc + parseInt(d), 0)
  }
  return n === 0 ? 1 : n
}

export function generateAngelSquare(targetNum) {
  if (!targetNum) return null

  const N = 6
  const totalCells = 36
  const handle = calculateHandle(targetNum)

  const door = (totalCells - 1) * handle
  const rawKey = ((2 * targetNum / N) - door) / 2
  const key = Math.floor(rawKey)

  const sequence = []
  for (let i = 0; i < totalCells; i++) {
    sequence.push(key + (i * handle))
  }

  const currentSum = (6 * key) + (105 * handle)
  const remainder = targetNum - currentSum

  const grid = Array.from({ length: 6 }, () => Array(6).fill(0))
  for (let row = 0; row < 6; row++) {
    for (let col = 0; col < 6; col++) {
      const sequenceIndex = SOLAR_TEMPLATE[row][col] - 1
      grid[row][col] = sequence[sequenceIndex]
    }
  }

  if (remainder !== 0) {
    for (let i = 0; i < 6; i++) {
      grid[i][i] += remainder
    }
  }

  return { grid, handle, key, door, remainder, lock: key + (35 * handle) }
}
