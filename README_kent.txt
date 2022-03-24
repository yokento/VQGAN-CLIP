open an anaconda shell and activate it to the VQGAN_Baker environment. cd to the directory this README is in.

	conda activate VQGAN_Baker

	cd C:\Users\yoken\Documents\GitHub\VQGAN-CLIP

make sure all 100 pre-bake images you want to bake are in the batch_input folder

	python generate_batch.py

this should put all 100 post bakes into the batch_output folder
