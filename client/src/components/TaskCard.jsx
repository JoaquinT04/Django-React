import { useNavigate } from 'react-router-dom'

export function TaskCard({ task }){
	
	const navigate = useNavigate()

	return (
		<div 
			style={{background:"black"}}
			onClick={()=>{
				navigate('/tasks/'+ task.id)
			}}
		>
			<hr />
			<h1>Titulo: {task.title}</h1>
			<h2>Descripcion:</h2>
			<p>{task.description}</p>
			<hr />
			<br />
		</div>
	)
}