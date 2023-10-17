import React from 'react'
import ChoreCard from './ChoreCard'

const ChoreContainer = (chores) => {

  function renderChores(){
    return (
      chores.map((chore))
    )
  }
  return (
    <>
    <ChoreCard />
    </>
  )
}

export default ChoreContainer