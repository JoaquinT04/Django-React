import { useEffect, useState } from 'react'
import { getAllTasks } from '../api/tasks.api'

export function TasksList(){
	const [tasks,setTasks]=useState([])


	useEffect( () => {
		async function loadTasks(){
			const res = await getAllTasks();
			setTasks(res.data);
		}
		
		loadTasks();

	}, [])

	return(
		<div>
			{tasks.map(task =>(
				<div>
					<h1>Titulo: {task.title}</h1>
					<h2>Descripcion:</h2>
					<p>{task.description}</p>
					<br />
				</div>
			))}
		</div>
	)
}