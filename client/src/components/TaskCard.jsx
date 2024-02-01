export function TaskCard({ task }){
	return (
		<div>
			<hr />
			<h1>Titulo: {task.title}</h1>
			<h2>Descripcion:</h2>
			<p>{task.description}</p>
			<hr />
			<br />
		</div>
	)
}