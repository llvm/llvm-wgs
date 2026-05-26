# Wednesday, March 20, 2024, 7:00 - 8:00 am PST

# Agenda

  316. New PR for the move is done. Zorg patches are up:


  1. [https://github.com/llvm/llvm-zorg/pull/141](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/141&sa=D&source=editors&ust=1779820787020249&usg=AOvVaw3WSvWnQlFKJzbd62h9gi1N) 
  2. [https://github.com/llvm/llvm-zorg/pull/142](https://www.google.com/url?q=https://github.com/llvm/llvm-zorg/pull/142&sa=D&source=editors&ust=1779820787020492&usg=AOvVaw1C-J8sqmc97KUE6pzl87BU)
  3. [https://github.com/llvm/llvm-project/pull/77154](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/77154&sa=D&source=editors&ust=1779820787020713&usg=AOvVaw0xRo3vjPQ-gNi-N0rInliJ) 
  4. [https://github.com/llvm/llvm-project/pull/75125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/75125&sa=D&source=editors&ust=1779820787020941&usg=AOvVaw1c5rvbBUc1O3vrd1N5j5ry)


  1. Llvm org mailing list


  317. PGO for GPUs is a working end-to-end prototype now


  1. [https://github.com/EthanLuisMcDonough/llvm-project/tree/gpuprofdriver](https://www.google.com/url?q=https://github.com/EthanLuisMcDonough/llvm-project/tree/gpuprofdriver&sa=D&source=editors&ust=1779820787021427&usg=AOvVaw39IDxk-Lw6Yh34bdy2Sfxc)
  2. # Compile with PGO instrumentation   
clang -L/dev/shm/YOURNAME/clang/install/lib -L/dev/shm/YOURNAME/clang/install/lib/x86_64-unknown-linux-gnu -fopenmp --offload-arch=native -fprofile-generate-gpu YOUR_FILE.c /dev/shm/YOURNAME/clang/install/lib/x86_64-unknown-linux-gnu/libomptarget.rtl.YOUR_GPU_TARGET.so  
# Reprocess data  
llvm-profdata merge YOUR_GPU_TARGET.default.profraw -o YOUR_GPU_TARGET.profdata  
# Recompile  
clang -L/dev/shm/YOURNAME/clang/install/lib -L/dev/shm/YOURNAME/clang/install/lib/x86_64-unknown-linux-gnu -fopenmp --offload-arch=native -fprofile-use-gpu=YOUR_GPU_TARGET.profdata YOUR_FILE.c


  318. Tablegen tooling update
  319. Testing


  1. Keep a list of issues we discuss in the meetings



# Make 1-3 people the "bug keepers"

* * *

#
