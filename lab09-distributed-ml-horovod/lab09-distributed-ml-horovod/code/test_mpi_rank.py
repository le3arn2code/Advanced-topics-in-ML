# nano code/test_mpi_rank.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f"Rank {rank} OK")
