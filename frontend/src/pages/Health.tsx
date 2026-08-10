import React from 'react'
import axios from 'axios'
import { useQuery } from '@tanstack/react-query'

async function fetchHealth() {
  const res = await axios.get('/health')
  return res.data
}

export default function Health() {
  const { data, isLoading, error } = useQuery(['health'], fetchHealth, {
    retry: 0,
  })

  if (isLoading) return <div>Loading health...</div>
  if (error) return <div>Error fetching health</div>

  return (
    <div>
      <h2>Backend Health</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}
