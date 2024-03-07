import { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { createTask,deleteTask, updateTask, getTask } from '../api/tasks.api'
import { useNavigate, useParams } from 'react-router-dom'
import { toast } from 'react-hot-toast'

export function TaskFormPage(){
	
	const { 
		register, 
		handleSubmit, 
		setValue,
		formState:{errors}
	} = useForm();

	const navigate = useNavigate();
	const params = useParams();
	console.log(params);

	const onSubmit = handleSubmit(async data => {
		if(params.id){
			console.log("actualizando");
			await updateTask(params.id,data)
			
			toast.success("Task updated",{
				position: "bottom-right",
				style:{
					background: "#140042",
					color: "#fff",
				}
			})

		}else{
			await createTask(data);
			
			toast.success("Task created",{
				position: "bottom-right",
				style:{
					background: "#140042",
					color: "#fff",
				}
			})
		}

		navigate('/tasks');
	})

	useEffect(()=>{
		async function loadTask(){
			if(params.id){
				console.log("obteniento datos")
				const { data:{title,description} }= await getTask(params.id)
				
				setValue('title',title)
				setValue('description',description)
			}
		}
		loadTask();
	},[])

	return(
		<div className='max-w-xl mx-auto'>
			<form onSubmit={onSubmit}>
				<input 
				className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'
				type="text" 
				placeholder="title" 
				{...register("title",{ required:true })}
				/>
				{errors.title && <span>title is required</span>}
				<textarea 
				className='bg-zinc-700 p-3 rounded-lg block w-full mb-3 h-full'
				rows="3" 
				placeholder="Description"
				{...register("description",{ required:true })}
				></textarea>

				{errors.description && <span>description is required</span>}

				<button
					className='bg-indigo-500 p-3 rounded-lg block w-full mt-3'>
				Guardar</button>
			</form>

		{params.id && (
		<div className='flex justify-end'>
				<button 
				className='bg-red-500 p-3 rounded-lg w-48 mt-3' 
				onClick={async ()=>{
					const acepted = window.confirm('estas seguro?')
					if(acepted){
						await deleteTask(params.id)
						navigate('/tasks')

						toast.success("Task deleted",{
							position: "bottom-right",
							style:{
								background: "#990000",
								color: "#fff",
							}
						})
					}
				}}
			>
				Delete
			</button>
		</div>
		)}

		</div>
	)
}